# -*- coding: utf-8 -*-

import scrapy

from pump_spider.items import PumpCoinsSpiderItem


class PumpCoinsSpider(scrapy.Spider):
    name = 'pump_coins_spider'
    redis_key = 'pump_coins_spider:start_urls'

    custom_settings = {
        'DOWNLOAD_DELAY': 5,
    }

    def start_requests(self):
        url = "https://frontend-api-v2.pump.fun/coins"
        headers = {
            "sec-ch-ua-platform": "ios",
            "Referer": "https://pump.fun/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "sec-ch-ua": "Google",
            "sec-ch-ua-mobile": "?0"
        }
        while True:
            params = {
                "offset": f"0",
                "limit": "20",
                "sort": "created_timestamp",
                "order": "DESC",
                "includeNsfw": "true"
            }
            yield scrapy.FormRequest(url, headers=headers, formdata=params, method='GET', dont_filter=True)

    def parse(self, response, **kwargs):
        raw_data_list = response.json()
        for data in raw_data_list:
            item = PumpCoinsSpiderItem()
            item.update(data)
            yield item
