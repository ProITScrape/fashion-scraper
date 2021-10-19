import scrapy
from scrapy import Request
from sources.items import  SourcesItem
import re
import json
from scrapy.utils.response import open_in_browser
from benedict import benedict
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BoohooSpider(scrapy.Spider):
    name = 'boohoo'
    
    custom_settings = {
            'FEED_FORMAT':'csv',
            'FEED_URI': 'boohoo_data.csv',
            'IMAGES_STORE' : 'boohooimages',
            'LOG_LEVEL' : 'ERROR', # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
            'LOG_FILE' :'boohoo.log'
        }

    start_urls = ['https://us.boohoo.com/womens']

    
    def parse(self, response):
        urls = response.xpath('//ol[@class="menu-section margin-bottom-20"]//li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url,callback = self.parse_results_page)
            #break
    
    def parse_results_page(self,response):
        next_page = response.xpath('//a[@title="Next"]/@href').extract_first()
        products_urls = response.xpath('//ul[@id="search-result-items"]/li[@class="grid-tile"]/div[@class="product-tile js-product-tile"]/meta[@itemprop="url"][1]/@content').getall()
        for p_url in products_urls:
            yield SeleniumRequest(url = p_url,callback = self.parse_product_page,wait_time=5,dont_filter= False,meta={"check":None},
                wait_until=EC.element_to_be_clickable((By.ID, 'thumbnails'))
            )
            #break
        if next_page :
            yield scrapy.Request(next_page, callback = self.parse_results_page)
            #pass
    def parse_product_page(self,response):
        #open_in_browser(response)
        item = SourcesItem()
        sub_category_1 = ""
        sub_category_2 = ""
        sub_category_3 = ""
        if response.meta['check'] == None:
            colors= response.xpath('//ul[@class="swatches color clearfix"]/li[contains(@class,"variation-value selectable variation-group-value")]/span/@data-swatch-product-url').getall()
            for color_url in colors:
                yield SeleniumRequest(url = color_url,callback = self.parse_product_page, wait_time = 5,dont_filter=True,meta={'check':False},
                wait_until=EC.element_to_be_clickable((By.ID, 'thumbnails')) )

        product_description =  response.xpath('//meta[@property="og:description"]/@content').extract_first()
        get_data = re.search(r'>pageContext =(.*?);<', response.body.decode("utf-8")).group(1)
        #get_data = response.xpath('//div[@id="pdpMain"]/@data-product-details-amplience').get()
        
        data = json.loads(get_data)
        data = data['analytics']['product']
        brand = data['brand']
        product_name = data['name']
        price = data['priceData']['price']['formatted']
        rating = ""
        review_count = ""
        color = response.xpath('//span[@class="attribute-title" and contains(text(),"Color:")]/following-sibling::span/text()').get().strip()
        fabric =  ""
        model_size = ""
        sizing = response.xpath('//ul[@class="swatches size clearfix"]//span[@class="swatchanchor-text"]//text()').getall()
        sizing = [ size.strip() for size in sizing]
        details_care = response.xpath('//h5[@id="ui-id-3" and contains(text(),"Details & Care")]/following-sibling::div//text()').get()
        if details_care :
            details_care = details_care.strip()
        
        meta_data_item={"description":product_description,
                    "brand":brand,
                    "name":product_name,
                    "price":price,
                    "rating":rating,
                    "reviews":review_count,
                    "colour":color,
                    "Kind of fabric":fabric,
                    "model size":model_size,
                    "sizing":sizing,
                    "details care":details_care
                    

                    }
        id_product = data['itemId']
        product_url= response.url
        adult_kid = "Adult"
        gender = data['dimension61'][0]
        main_category  = data['categoryPath'][0]['displayName']
        try:
            sub_category_1 = data['categoryPath'][1]['displayName']
            sub_category_2 = data['categoryPath'][2]['displayName']
            sub_category_3 = data['categoryPath'][3]['displayName']
        except Exception:
            pass
        image_urls = []
        get_images = response.xpath('//img[@data-lgimg]')
        for img in get_images:
            img =  img.xpath('./@data-lgimg').extract_first()
            imgs_json = json.loads(img)
            image_urls.append(imgs_json['url'])
        image_names = []
        for i,img in enumerate(image_urls):
            image_name= "{category}_{sub_cat1}_{sub_cat2}_{product_name}_{id}_{color}_{index}.jpg".format(category=main_category,sub_cat1=sub_category_1,sub_cat2=sub_category_2,product_name=product_name,index = i,id=id_product,color=color)
            image_name=re.sub('[^A-Za-z0-9_^-^.]+', '-', image_name)
            image_names.append(image_name)
        images_number = len(image_urls)
        image_name= "{category}_{sub_cat1}_{sub_cat2}_{product_name}_{id}_{color}".format(category=main_category,sub_cat1=sub_category_1,sub_cat2=sub_category_2,product_name=product_name,id=id_product,color=color)
        image_name=re.sub('[^A-Za-z0-9_^-^.]+', '-', image_name)
        person_height = ""
        cloth_size_in_image = ""
        cloth_length_in_image = ""
        item['id_product']=id_product
        item['page_url']= product_url
        item['adult_kid'] = adult_kid
        item['gender'] = gender
        item['category']= main_category
        item['subcategory1']= sub_category_1
        item['subcategory2']= sub_category_2
        item['subcategory3']= sub_category_3
        item['price'] = price
        item['measuring_unit'] = "in"
        item['person_height'] = person_height
        item['cloth_size_in_image']= cloth_size_in_image
        item['cloth_length_in_image'] = cloth_length_in_image
        item['number_of_images_on_page'] = images_number
        item['image_names'] = image_names
        item['meta']= meta_data_item
        item['image_name'] = image_name
        item['image_urls'] = image_urls
        yield item

