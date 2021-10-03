import scrapy
import re
import json
from benedict import benedict

class TestItSpider(scrapy.Spider):
    name = 'test_it'
   
    start_urls = ['https://www.shein.com/Clothing-c-2030.html']

    def parse(self, response):
        data=re.search(r'gbProductListSsrData = (.*?)\n', response.body.decode("utf-8")).group(1)
        data = json.loads(data)
        data=data['results']['filterCates']['children']
        for cat in data:
            cat_id = cat['cat_id']
        d = benedict(data)
        cats =d.search('cat_id', in_keys=True, exact=True, case_sensitive=False)
        print ("hhhh",cats)
            
