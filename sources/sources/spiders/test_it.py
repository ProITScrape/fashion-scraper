import scrapy
import re
import json
from benedict import benedict
from scrapy import Request
class TestItSpider(scrapy.Spider):
    name = 'test_it'
    attr_items=[]
    custom_settings ={
        "FEED_EXPORT_FIELDS":['url',"count"]

    }    
    start_urls = ['https://www.shein.com/Clothing-c-2030.html']
    def get_children(self,json_input,cats):
        cat_id = json_input['cat_id']
        if "children" in json_input.keys():
            for e in json_input['children']:
                cat_id = e['cat_id']
                cats= self.get_children(e,cats)
        else:
            cats.append(cat_id)
        return cats

    url= "https://www.shein.com/Clothing-c-2030.html?child_cat_id=1733&attr_ids=27_118-87_568"
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
    
    def refine(self,response):
        get_product_count = response.xpath('//span[@class="top-info__title-sum"]/text()').get()
        product_count = [int(i) for i in get_product_count.split() if i.isdigit()]
        if product_count:
            product_count = product_count[0]
            if product_count <=4800:
                yield {"url":response.url,"count":product_count}
            else:
                index = response.meta['index']+1
                attr = self.attr_items[index]
                attr_values = attr['values']
                for attr_value in attr_values:
                    url= response.url+"-"+attr_value['id']
                    meta ={"index":index}
                    yield Request(url,meta=meta,callback= self.refine)
        
    def parse(self, response):
        all_attrs =[]
        all_cats = []
        data=re.search(r'gbProductListSsrData = (.*?)\n', response.body.decode("utf-8")).group(1)
        data = json.loads(data)
        filter_cates=data['results']['filterCates']['children']
        for cat in filter_cates:
           cats = []
           all_cats += self.get_children(cat,cats)
        print (all_cats)
        filter_attrs = data['results']['filterAttrs'] 
        for filter_attr in filter_attrs:
            attr_name =  filter_attr['attr_name']
            attrs = []
            all_attrs = self.get_attr_ids(filter_attr, attrs)
            attr_item={"filterName":attr_name,"values":all_attrs}
            self.attr_items.append(attr_item)

        #print (json.dumps(items))
        for cat in all_cats:
            for attr in self.attr_items:
                attr_values = attr['values']
                for attr_value in attr_values:
                    meta={"index":0}
                    url = "https://www.shein.com/Clothing-c-2030.html?child_cat_id={cat}&attr_ids={attr_value}".format(cat=cat, attr_value = attr_value['id'])
                    yield Request(url, callback= self.refine,meta=meta)
                    

           
        """cat_id = cat['cat_id']
            if "children" in cat.keys():
                for cat_ch in cat['children']:
                    cat_ch_id = cat_ch['cat_id']
                    if "children" in cat_ch.keys():
                        for cat_ch_ch in cat_ch['children']:
                            cat_ch_ch_id = cat_ch_ch['cat_id']
                            if "children" in cat_ch_ch.keys():
                            for cat_ch_ch_ch in cat_ch_ch['children']:
                                cat_ch_ch_ch_id = cat_ch_ch_ch['cat_id']
        """            
        
            
