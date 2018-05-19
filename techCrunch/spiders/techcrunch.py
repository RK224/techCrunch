# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpider(scrapy.Spider):
    name = "techcrunch"
    start_urls = (
        'https://techcrunch.com/feed/',
    )

    custom_settings = {
    	'FEED_URI' : "tmp/techCrunch.jl"
	}
    def parse(self, response):
    	response.selector.remove_namespaces()
    	titles = response.xpath('//item/title/text()').extract()
    	publishing_dates = response.xpath("//item/pubDate/text()").extract()
    	authors = response.xpath('//item/creator/text()').extract()

    	for article in zip(titles,publishing_dates,authors):
    		yield {
    			"article title" : article[0],
    			"published on"	: article[1],
    			'author' : article[2]
    			}