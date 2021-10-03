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
    def parse(self, response):
        data=re.search(r'gbProductListSsrData = (.*?)\n', response.body.decode("utf-8")).group(1)
        data = json.loads(data)
        data=data['results']['filterCates']['children']
        for cat in data:
            cats = []
            print(self.get_children(cat,cats))
            
            
            
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
        
            
