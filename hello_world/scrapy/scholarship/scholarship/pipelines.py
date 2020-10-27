# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import openpyxl

class ScholarshipPipeline:
    def __init__(self):
        # self.f = open("URL.json","wb")
        self.spider = None
        self.count = 0

    def open_spider(self, spider):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['title', 'url'])

    def process_item(self, item, spider):
        # content = json.dumps(dict(item),ensure_ascii=False) + ","
        # self.f.write(content.encode())
        # return item
        line = [item['title'],item['needURL']]
        self.ws.append(line)
        return item

    def close_spider(self,spider):
        # self.f.close()
        self.wb.save("geturl.xlsx")