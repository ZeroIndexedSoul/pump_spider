# -*- coding: utf-8 -*-

import scrapy
from scrapy_redis.spiders import RedisSpider

from pump_spider.items import PumpCoinsSpiderItem


class PumpCoinsUpdateSpider(RedisSpider):
    name = 'pump_coins_update_spider'
    redis_key = 'pump_coins_update_spider:search_mint'

    custom_settings = {
        'DOWNLOAD_DELAY': 0,
        'CONCURRENT_REQUESTS': 128,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 128,
        'CONCURRENT_REQUESTS_PER_IP': 128,
        'RETRY_TIMES': 3,
        'RETRY_DELAY': 0,
        'COOKIES_ENABLED': False,
        'DOWNLOAD_TIMEOUT': 5
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh,zh-CN;q=0.9,en-GB;q=0.8,en;q=0.7,zh-HK;q=0.6",
        "cache-control": "max-age=0",
        "cookie": "_ga=GA1.1.478290472.1732012135; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZGRyZXNzIjoiRFpvTE5rOFI0ZkFHOEJIb0E4czdBV1FUMTl0VTRIMXFFTW9SRXZieWR1TmsiLCJyb2xlcyI6WyJ1c2VyIl0sImdyb3VwIjoidGVzdCIsImVyYSI6IkZFQVRVUkVEIHYxLjYiLCJlcmFzIjpbeyJlcmEiOiJGRUFUVVJFRCB2MS42IiwiZ3JvdXAiOiJ0ZXN0In0seyJlcmEiOiJTRUFSQ0h2MS4wTUVUQVN2MS4wIiwiZ3JvdXAiOiJ0ZXN0In0seyJlcmEiOiJUUkVORElOR19DQVJPVVNFTHYxLjAiLCJncm91cCI6ImNvbnRyb2wifSx7ImVyYSI6IldBVENITElTVHYxLjAiLCJncm91cCI6ImNvbnRyb2wifV0sImlhdCI6MTczNTAxMTY5MywiZXhwIjoxNzM3NjAzNjkzfQ.parLtZL6_E6DhmhhbRSHQBOiNDqIfYCu0ncnTIEhhxE; __cf_bm=HcJ4_qipZGsOdBWrTTJoW4buuNmxU9YjFbOofcml1gE-1735267313-1.0.1.1-b_xAqhj26pQ.7LORaQTcYljCK7q42MqdeyBH5zVCCAA0cA7wy_OxFtkBcsiue24W5_cwx34UWXvmMVwXxDHs6w; cf_clearance=Q_J88CXkbwYlPVfRGLysp6hUl1KoR2EoSxhNaxsSin4-1735267314-1.2.1.1-rIZW28SxO4OZdf4r7vH_WVIU6b_lkTXemVS3JfVxJ15uoc1uaOxZnjMiKoOc6hFRz5NHt9rzXDzMaurGEkKBUV4z2tmsLck0IiHA5hZZE6hZfH5GH1Nx8_G8mfOGVzGyXFRVbX3wsLRVlbS3TaD1T4QM593jdrOtqDLEl6bccSRUQCHyUmYrA0DKu2UD_Cg5lsnfgNrH_ZTPQ0RxSOPscfPOgkm1uQMj0XJ4whdF_J1InvPas9DPJ3V4twRTVf.js1INhxDsiyAKOAcXuo.KxaLnsL1jJjDoTMe7sE9HFPO9jZI.Z.80g_NbHDrcg.jW2UMAHMtBDRgKqMaVmFEnjM.l7vPXZv_77nHJxdhGhWhaqvqh52d8bWZwggkCQ8N0mVcvXkvb9MYqN_8lmbvOdw; fs_uid=#o-1YWTMD-na1#32f1cd0d-c220-47b3-9f52-f69a199f0511:f8499134-aa40-464f-9fa5-21a90bb4d1a2:1735267320284::2#1e3f6cd4#/1763780765; fs_lua=1.1735267658635; _ga_T65NVS2TQ6=GS1.1.1735267319.44.1.1735267845.60.0.0",
        "if-none-match": "W477-2YUUbr2ssdR+I78FG1Tg8PwLB2Q",
        "priority": "u=0, i",
        "sec-ch-ua": "Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    url = "https://frontend-api-v2.pump.fun/coins"

    def make_request_from_data(self, data):
        if isinstance(data, bytes):
            data = data.decode('utf-8')
        search_mint = data  # mint
        params = {
            "offset": "0",
            "limit": "50",
            "searchTerm": search_mint,
        }
        yield scrapy.FormRequest(self.url, headers=self.headers, formdata=params, method='GET', dont_filter=True)

    def parse(self, response, **kwargs):
        raw_data_list = response.json()
        for data in raw_data_list:
            item = PumpCoinsSpiderItem()
            item.update(data)
            yield item
