import scrapy
#导入items file中的ScholarshipTiem class
from ..items import ScholarshipItem

class GeturlSpider(scrapy.Spider):
    #spider name 爬虫名
    name = 'geturl'
    #allowed domains 允许的域名
    allowed_domains = ['www.ptu.edu.cn']
    baseURL = "http://www.ptu.edu.cn/index/xngg/"
    offset = 1
    ENDURL = ".htm"
    #start_url起始的网站地址
    start_urls = [baseURL + str(offset) +ENDURL]
    def parse(self, response):
        #通过xpath实现，寻找所需要的数据
        node_list = response.xpath("/html/body/div[4]/div/div/div[2]/ul/li/a")
        for node in node_list:
            ul = "www.ptu.edu.cn"
            item = ScholarshipItem()#使用导入的ScholarshipTiem class
            #获取所需的title数据
            item['title'] = node.xpath("./text()").extract()[0]
            #获取所需的URL数据
            item['needURL'] = ul + node.xpath("./@href").extract()[0]
            #返回item到pipeline，通过pipline处理所获取的数据
            yield item
            if self.offset < 105:#翻页条件
                self.offset += 1
                #next_url 下一页的URL
                next_url = self.baseURL +str(self.offset) + self.ENDURL
                yield scrapy.Request(next_url, callback = self.parse)
            else:
                #爬虫结束
                print('crawl over!')
