
import scrapy
from scrapy.crawler import CrawlerProcess

from sources.spiders.shein_goods  import SheinGoodsSpider
from sources.spiders.shein_goods1  import SheinGoods1Spider
from sources.spiders.shein_goods2  import SheinGoods2Spider
from sources.spiders.shein_goods3  import SheinGoods3Spider
from sources.spiders.shein_goods4  import SheinGoods4Spider
from scrapy.utils.project import get_project_settings
import pkgutil
import datetime
settings = get_project_settings()
goods_urls=[]
input_file =pkgutil.get_data("sources", "/urls.csv").decode('utf8')

rows = input_file.splitlines()
for row in rows :
    goods_urls.append(row)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(goods_urls), n):
        yield lst[i:i + n]

if len(goods_urls)%5==0:
    n=len(goods_urls)/5
else:
    n=len(goods_urls)//5+1 
   
goods_list=list(chunks(goods_urls, int(n)))  
#print(test_list)   
process = CrawlerProcess(get_project_settings())
#process = CrawlerProcess()
spider = SheinGoodsSpider
spider1 = SheinGoods1Spider
spider2 = SheinGoods2Spider
spider3 = SheinGoods3Spider
spider4 = SheinGoods4Spider

try:     
    process.crawl(spider,goods_urls=goods_list[0],gender="F",adult_kid="Adult")
    process.crawl(spider1,goods_urls=goods_list[1],gender="F",adult_kid="Adult")
    process.crawl(spider2,goods_urls=goods_list[2],gender="F",adult_kid="Adult")
    process.crawl(spider3,goods_urls=goods_list[3],gender="F",adult_kid="Adult")
    process.crawl(spider4,goods_urls=goods_list[4],gender="F",adult_kid="Adult")
    
except IndexError:
    pass
    

e=datetime.datetime.now()
process.start() # the script will block here until all crawling jobs are finished
f=datetime.datetime.now()
print(f-e)    