# -*- coding: utf-8 -*-
import scrapy


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather,com']
    start_urls = ['https://weather.com/en-IN/weather/tenday/l/INMP0380:1:IN']

    def parse(self, response):
        #each_row=response.xpath('//tr[contains(@class,("clickable")) and contains(@class,"open"))]/td@title')
        #yield {'Location':response.xpath('//div[contains(@class,"locations-title ten-day-page-title")]/h1/text()')[0].extract()}
        #yield {'Time': response.xpath('//div[contains(@class,"observation-timestamp")]/span/text()')[0].extract()}
        data=response.css('tr.clickable')
        for i in data:
            item= {
                'Time': response.xpath('//div[contains(@class,"observation-timestamp")]/span/text()')[0].extract(),
                'Day': i.css('tr div div span::text').extract_first(),
                'Date': i.css('tr div span.day-detail.clearfix ::text').extract_first(),
                'Description': i.css('td.description span ::text').extract_first(),
                'MAX temp (deg Celcius)': i.css('td.temp div span::text')[0].extract(),
                'MIN temp (deg Celcius)': i.css('td.temp div span::text')[1].extract(),   
                'Precipitation (in %)': i.css('td.precip div span span::text').extract_first(),
                'Wind': i.css('td.wind span::text').extract_first(),
                'Humidity (in %)': i.css('td.humidity span span::text').extract_first(),
                'Other Details': i.css('td.humidity ::attr(title)').extract_first(),
                'Location':response.xpath('//div[contains(@class,"locations-title ten-day-page-title")]/h1/text()')[0].extract(),

            }
            yield item