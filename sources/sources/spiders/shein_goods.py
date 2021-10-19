import scrapy
from scrapy import Request
from sources.items import  SourcesItem
import re
import json
from scrapy.utils.response import open_in_browser
from benedict import benedict

class SheinGoodsSpider(scrapy.Spider):
    name = 'shein_goods'
    custom_settings = {
            'FEED_FORMAT':'csv',
            'FEED_URI': 'shien_data.csv',
            'IMAGES_STORE' : 'sheinimages'
        }
    def __init__(self,goods_urls,*args, **kwargs):
        self.goods_urls = goods_urls   

    def start_requests(self):
        for url in self.goods_urls:
            meta={"productUrl":url}
            yield scrapy.Request(url,callback = self.parse_goods,meta=meta)

    
    def get_adult_kid_gender(self, categories, name):
        match = categories+[name]
        women =["girl","women"]
        men= ['men',"boy"]
        kid = ["girl","boy"]
        adult = ["men","women"]
        for v in women:
            for c in match:
                if v in c.lower().split():
                    gender = "F"
                    break
        for v in men:
            for c in match:
                if v in c.lower().split():
                    gender = "M"
                    break          
        for v in adult:
            for c in match:
                if v in c.lower().split():
                    adult_kid = "Adult"
                    break
        for v in kid:
            for c in match:
                if v in c.lower().split():
                    adult_kid = "kid"
                    break
        return gender, adult_kid            
        

    def parse_goods(self, response):
        #open_in_browser(response)
        rating = ""
        review_count = ""
        sub_category_2 = ""
        model_size = ""
        sub_category_3 = ""
        cloth_length_in_image = ""
        price = ""
        person_height =""
        cloth_size_in_image = ""
        item = SourcesItem()
        product_data=re.search(r'productIntroData:(.*?),\n        abt:', response.body.decode("utf-8")).group(1)
        data = json.loads(product_data)
        d = benedict(data['parentCats'])
        cats =d.search('cat_url_name', in_keys=True, exact=True, case_sensitive=False)
        categories = [cat[0]['cat_name'] for cat in cats]
        categories=list(dict.fromkeys(categories))
        product_name = data['detail']['goods_name']
        id_product =  data['detail']['goods_id']
        main_category = data['parentCats']['cat_name']
        #adult,gender
        gender,adult_kid = self.get_adult_kid_gender(categories,product_name)
        
        try:
            sub_category_1=categories[1]
            sub_category_2=categories[2]
            sub_category_3=categories[3]
        except Exception:
            pass     
        try: 
            model_size= data['model']['size']
        except Exception:
            pass
        try:
            price =data['detail']['salePrice']['amountWithSymbol'].replace('US','')
        except Exception:
            pass
        try :
            person_height = data['model']['attrcm']['Height'].replace('cm',"").strip()
        except Exception:
            pass
        try:
            cloth_size_in_image = data['model']['size'].replace('cm',"").strip().strip()
            cloth_length_in_image = data['sizeInfoDes']["sizeInfo"][[r['size']=="%s"%cloth_size_in_image for r in data['sizeInfoDes']["sizeInfo"]].index(True)]['Lengte '].replace('cm','').strip()
        except Exception:
            pass
        image_names = []
        more_imgs= ["https:"+img['image_url'] for img in data['more_goods_imgs']]
        list_images = ["https:"+data['goods_imgs']['main_image']['origin_image']]+["https:"+img['origin_image'] for img in data['goods_imgs']['detail_image'] ]
        
        list_images = list_images + more_imgs 
        for index, image_url in enumerate(list_images):
            image_name = "{code}_{gender}_{category}_{sub_category1}_{sub_category2}_{product_name}_{index}.jpg".format(gender=gender.lower(),category=main_category,sub_category1=sub_category_1,sub_category2=sub_category_2,product_name = product_name,code=id_product,index=index+1).replace(' ',"-")
            image_name=re.sub('[^A-Za-z0-9_^-^.]+', '-', image_name)
            image_names.append(image_name)
        image_name = "{code}_{gender}_{category}_{sub_category1}_{sub_category2}_{product_name}".format(gender=gender.lower(),category=main_category,sub_category1=sub_category_1,sub_category2=sub_category_2,product_name=product_name,code=id_product).replace(' ',"-")
        image_name = re.sub('[^A-Za-z0-9_^-^.]+', '-', image_name)
        
        images_number = len(list_images)
        ###
        product_description =data['detail']['goods_desc']
        brand = data['detail']['brand']
        try:
            rating= data['commentInfo']['comment_rank_average']
            review_count = data['commentInfo']['comment_num']
        except Exception:
            pass    
        e = data['detail']
        color =""
        fabric= ""
        try:
            desc_values=[{e["attr_name_en"]:e['attr_value_en']} for e in e['productDetails']]
        except Exception:
            pass
        
        try:
            color =  [t['attr_value_en'] for t in e["productDetails"] if t['attr_name_en']=="Color"] 
        except Exception:
            pass
        
        try:    
            fabric = [t['attr_value_en'] for t in e["productDetails"] if t['attr_name_en']=="Fabric"] 
        except Exception:
            pass    
        try:
            material =  [t['attr_value_en'] for t in e["productDetails"] if t['attr_name_en']=="Material"] 
            if not material:
                material =  [t['attr_value_en'] for t in e["productDetails"] if t['attr_name']=="Materiaal"]
        except Exception:
            pass
        try:
            composition=[t['attr_value_en'] for t in e["productDetails"] if t['attr_name_en']=="Composition"] 
        except Exception:
            pass

        p_url= "https://nl.shein.com/{url_name}-p-{goods_id}-cat-{cat}.html"
        related_urls = [p_url.format(url_name=re.sub(' +', '-',p["goods_url_name"]),goods_id=p["goods_id"],cat=p['cat_id']) for p in data['relation_color']]
        for url in related_urls:
            yield Request(url = url,
                callback = self.parse_goods,
                meta= {"productUrl":url}
            )
        meta_data_item={"description":product_description,
                    "brand":brand,
                    "name":product_name,
                    "price":price,
                    "rating":rating,
                    "reviews":review_count,
                    "colour":color,
                    "Kind of fabric":fabric,
                    "model size":model_size,
                    "sizing":data['sizeInfoDes']['sizeInfo'],
                    "material":material,
                    "composition":composition,
                    "description values":desc_values

                    }
        
        item['id_product']=id_product
        item['page_url']= response.meta['productUrl']
        item['adult_kid'] = adult_kid
        item['gender'] = gender
        item['category']= main_category
        item['subcategory1']= sub_category_1
        item['subcategory2']= sub_category_2
        item['subcategory3']= sub_category_3
        item['price'] = price
        item['measuring_unit'] = "cm"
        item['person_height'] = person_height
        item['cloth_size_in_image']= cloth_size_in_image
        item['cloth_length_in_image'] = cloth_length_in_image
        item['number_of_images_on_page'] = images_number
        item['image_names'] = image_names
        item['meta']= meta_data_item
        item['image_name'] = image_name
        item['image_names'] = image_names
        item['image_urls'] = list_images
        yield item



