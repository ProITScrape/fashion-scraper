import scrapy
import re
import json

class TestItSpider(scrapy.Spider):
    name = 'test_it'
   
    start_urls = ['https://www.shein.com/Clothing-c-2030.html']

    def parse(self, response):
        data=re.search(r'gbProductListSsrData = (.*?)\n', response.body.decode("utf-8")).group(1)
        data = json.loads(data)
        print (data.keys())
     
