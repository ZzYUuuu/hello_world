# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import openpyxl#使用xls来保存数据

class ScholarshipPipeline:
    def __init__(self):#初始化条件
        # self.f = open("URL.json","wb")
        self.spider = None
        self.count = 0

    def open_spider(self, spider):#初始化xls的页面
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['title', 'url'])#所包含的两个value值的key

    def process_item(self, item, spider):#存入数据
        # content = json.dumps(dict(item),ensure_ascii=False) + ","
        # self.f.write(content.encode())
        # return item
        line = [item['title'],item['needURL']]
        self.ws.append(line)
        return item

    def close_spider(self,spider):#关闭spider
        # self.f.close()
        self.wb.save("geturl.xlsx")#保存数据