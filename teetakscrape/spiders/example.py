# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['teetak.gr']
    start_urls = ['http://teetak.gr/']

    def parse(self, response):
        pass
