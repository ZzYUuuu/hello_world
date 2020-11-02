# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScholarshipItem(scrapy.Item):
    #title 标题
    title = scrapy.Field()
    #needURL 所需要的URL
    needURL = scrapy.Field()
