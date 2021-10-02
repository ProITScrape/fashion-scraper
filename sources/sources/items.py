# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SourcesItem(scrapy.Item):
    image_urls = scrapy.Field()
    image_name = scrapy.Field()
    images = scrapy.Field()
    id_product =scrapy.Field()
    page_url= scrapy.Field()
    adult_kid = scrapy.Field()
    gender =scrapy.Field()
    category =scrapy.Field()
    subcategory1 =scrapy.Field()
    subcategory2 =scrapy.Field()
    subcategory3 =scrapy.Field()
    price =scrapy.Field()
    person_height=scrapy.Field()
    cloth_size_in_image = scrapy.Field()
    cloth_length_in_image = scrapy.Field()
    number_of_images_on_page = scrapy.Field()
    meta =scrapy.Field()
    image_names = scrapy.Field()
    measuring_unit =scrapy.Field()
