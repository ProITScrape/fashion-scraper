import scrapy
import re
import json
from benedict import benedict
from scrapy import Request
class SheinUrlsSpider(scrapy.Spider):
    name = 'shein_urls'
    all_urls = []
    attr_items=[]
    custom_settings ={
        "FEED_EXPORT_FIELDS":['url']}
        
    start_urls = ['https://nl.shein.com/Clothing-c-2030.html']
    def get_children(self,json_input,cats):
        cat_id = json_input['cat_id']
        if "children" in json_input.keys():
            for e in json_input['children']:
                cat_id = e['cat_id']
                cats= self.get_children(e,cats)
        else:
            cats.append(cat_id)
        return cats

    def get_attr_ids(self,json_input, attrs):
        if json_input["attr_values"]:
            for attr in  json_input['attr_values']:
                item={"id":attr['attr_filter'], "name":attr['attr_value']}
                attrs.append(item)
        if json_input["groups"]:
            for attr in  json_input['groups']:
                for attr in attr['attr_values']:
                    item={"id":attr['attr_filter'], "name":attr['attr_value']}
                    attrs.append(item)
        return attrs
    
    def parse_category(self, response):
        get_prodcuts = re.search(r'gbProductListSsrData =(.*?)\n', response.body.decode("utf-8"))
        if get_prodcuts:
            get_prodcuts = get_prodcuts.group(1).strip()
            data = json.loads(get_prodcuts)
            goods = data["results"]['goods']
            if goods:
                for goods_item in goods:
                    product_url = "https://nl.shein.com"+goods_item['pretreatInfo']['goodsDetailUrl']
                    if product_url  not in self.all_urls:
                        yield {"url":product_url}
                        self.all_urls.append(product_url)
                next_page = response.meta['page']+1
                next_page_url =response.meta['url']+str(next_page)
                meta ={"url":response.meta['url'],"page":next_page}
                yield scrapy.Request(next_page_url,callback=self.parse_category,meta=meta)
                    

    def refine(self,response):
        get_product_count = response.xpath('//span[@class="top-info__title-sum"]/text()').get()
        product_count = [int(i) for i in get_product_count.split() if i.isdigit()]
        if product_count:
            product_count = product_count[0]
            if product_count <=4800:
                url = response.url+"&page="
                meta={"url":url,"page" :1}
                yield scrapy.Request(url,callback = self.parse_category,dont_filter=True,meta=meta)
            else:
                index = response.meta['index']+1
                attr = self.attr_items[index]
                attr_values = attr['values']
                for attr_value in attr_values:
                    if response.meta['query']:
                        query=response.meta['query']+"-"+attr_value['id']
                    else:
                        query=attr_value['id']
                    url= response.meta['url']+query
                    meta ={"index":index,"url":response.meta['url'],"query":query}
                    yield Request(url,meta=meta,callback= self.refine)
        
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback = self.parse,meta={"url":url})
    
    def parse(self, response):
        all_attrs =[]
        all_cats = []
        data=re.search(r'gbProductListSsrData = (.*?)\n', response.body.decode("utf-8")).group(1)
        data = json.loads(data)
        filter_cates=data['results']['filterCates']['children']
        for cat in filter_cates:
           cats = []
           all_cats += self.get_children(cat,cats)
        filter_attrs = data['results']['filterAttrs'] 
        for filter_attr in filter_attrs:
            attr_name =  filter_attr['attr_name']
            attrs = []
            all_attrs = self.get_attr_ids(filter_attr, attrs)
            attr_item={"filterName":attr_name,"values":all_attrs}
            self.attr_items.append(attr_item)

        for cat in all_cats:
            url = "{url}?child_cat_id={cat}&attr_ids=".format(cat=cat,url = response.meta['url'])
            meta={"index":-1,"url":url,"query":""}
            yield Request(url, callback= self.refine,meta=meta)
                    

           
        
            
