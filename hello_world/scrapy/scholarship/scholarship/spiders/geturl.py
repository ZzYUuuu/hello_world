import scrapy
from ..items import ScholarshipItem

class GeturlSpider(scrapy.Spider):
    name = 'geturl'
    allowed_domains = ['www.ptu.edu.cn']
    baseURL = "http://www.ptu.edu.cn/index/xngg/"
    offset = 1
    ENDURL = ".htm"
    start_urls = [baseURL + str(offset) +ENDURL]
    def parse(self, response):
        node_list = response.xpath("/html/body/div[4]/div/div/div[2]/ul/li/a")
        for node in node_list:
            ul = "www.ptu.edu.cn"
            item = ScholarshipItem()
            item['title'] = node.xpath("./text()").extract()[0]
            item['needURL'] = ul + node.xpath("./@href").extract()[0]
            yield item
            if self.offset < 105:
                self.offset += 1
                next_url = self.baseURL +str(self.offset) + self.ENDURL
                yield scrapy.Request(next_url, callback = self.parse)
            else:
                print('crawl over!')
