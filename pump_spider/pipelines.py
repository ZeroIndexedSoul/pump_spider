# -*- coding: utf-8 -*-
import datetime
import json

import redis

from scrapy.utils.project import get_project_settings


class PumpSpiderPipeline:
    settings = get_project_settings()
    redis_config = {
        "host": settings.get("REDIS_HOST"),
        "port": settings.get("REDIS_PORT"),
        "db": settings.get("REDIS_DB")
    }

    def __init__(self):
        self.redis_client = redis.StrictRedis(**self.redis_config, decode_responses=True)

    def process_item(self, item, spider):
        # created_timestamp 1736223049599
        mint = item["mint"]
        created_timestamp = item["created_timestamp"]
        date_time = datetime.datetime.fromtimestamp(created_timestamp / 1000)
        date_time_str = date_time.strftime('%Y-%m-%d')
        coin_data = json.dumps(dict(item))
        self.redis_client.hset(f"pump_coins_data:{date_time_str}", key=mint, value=coin_data)
        self.redis_client.hset(f"pump_coins_data", key=mint, value=coin_data)
        spider.logger.info(f"Success save data,created_timestamp:{created_timestamp}, mint:{mint}")
        return item
