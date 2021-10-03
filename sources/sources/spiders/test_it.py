import scrapy
import re
import json
from benedict import benedict

class TestItSpider(scrapy.Spider):
    name = 'test_it'
   

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

    def get_attr_ids(self,json_input, attrs):
        if json_input["attr_values"]:
            for attr in  json_input['attr_values']:
                item={"id":attr['attr_filter'], "name":attr['attr_value']}
                attrs.append(item)
        if json_input["groups"]:
            for attr in  json_input['groups']:
                for attr in attr['attr_values']
                    item={"id":attr['attr_filter'], "name":attr['attr_value']}
                    attrs.append(item)
        return attrs

    def parse(self, response):
        data=re.search(r'gbProductListSsrData = (.*?)\n', response.body.decode("utf-8")).group(1)
        data = json.loads(data)
        filter_cates=data['results']['filterCates']['children']
        for cat in filter_cates:
            cats = []
            print(self.get_children(cat,cats))
            
        filter_attrs = data['results']['filterAttrs'] 
        for filter_attr in filter_attrs:
            attrs =[]
            print (self.get_attr_ids(self,filter_attr, attrs))

            
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
        
            
