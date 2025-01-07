# -*- coding: utf-8 -*-

import random
from scrapy.utils.project import get_project_settings


class PumpSpiderDownloaderMiddleware:
    settings = get_project_settings()

    PROXY_IP_LIST = settings.get("PROXY_IP_LIST", [])

    def process_request(self, request, spider):
        if self.PROXY_IP_LIST:
            proxy = random.choice(self.PROXY_IP_LIST)
            request.meta['proxy'] = f'http://{proxy}'
            spider.logger.debug(f"{spider.name} use proxy")
        return None
