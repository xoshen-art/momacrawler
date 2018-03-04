# -*- coding: utf-8 -*-
import scrapy


class MomaspiderSpider(scrapy.Spider):
  name = 'momaspider'
  start_urls = ['http://www.moma.org/calendar/exhibitions/1?locale=en']

  def start_requests(self):
    for i in range(1, 1219):
      url = "https://www.moma.org/calendar/exhibitions/EX_NUM?locale=en".replace("EX_NUM", str(i))
      yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
      yield { 'description': response.css('meta[name=description]::attr(content)').extract() }
                