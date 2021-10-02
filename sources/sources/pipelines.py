# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from urllib.parse import urlparse
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class SourcesPipeline:
    def process_item(self, item, spider):
        return item

class CustomImageNamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'image_name': item["image_name"]+"_"+str(index+1)})
                for index,x in enumerate(item.get('image_urls', []))]

    def file_path(self, request, response=None, info=None):
        return 'full/%s.jpg' % request.meta['image_name']
