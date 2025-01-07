from datetime import datetime

import redis

from pump_spider.settings import REDIS_HOST, REDIS_PORT, REDIS_DB


class PushUpdateCoinsRequests:
    """Push the coins mint address that needs to be updated."""
    redis_key = 'pump_coins_update_spider:search_mint'

    redis_config = {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": REDIS_DB
    }

    def __init__(self):
        self.redis_client = redis.StrictRedis(**self.redis_config, decode_responses=True)

    def get_mints_by_date(self, date_time_str=None) -> list:
        """
        Retrieves the mint keys from Redis for a specific date.

        Args:
            date_time_str (str, optional): The date in 'YYYY-MM-DD' format. If None, the current date will be used.

        Returns:
            list: A list of mint keys (strings) for the given date.

        Raises:
            ValueError: If date_time_str is provided and does not match the 'YYYY-MM-DD' format.
        """
        if date_time_str is None:
            date_time_str = datetime.today().strftime('%Y-%m-%d')
        else:
            # 验证date_time_str 是否是 '%Y-%m-%d'
            try:
                datetime.strptime(date_time_str, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format. Expected 'YYYY-MM-DD'.")
        mints = self.redis_client.hkeys(f"pump_coins_data:{date_time_str}")
        return mints

    def run(self):
        mint_list = self.get_mints_by_date()
        if mint_list:
            self.redis_client.lpush(self.redis_key, *mint_list)
            print(f'success push {len(mint_list)} mint')
        else:
            print(f'not mint data')


if __name__ == '__main__':
    PushUpdateCoinsRequests().run()
