# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PumpCoinsSpiderItem(scrapy.Item):
    mint = scrapy.Field()
    name = scrapy.Field()
    symbol = scrapy.Field()
    description = scrapy.Field()
    image_uri = scrapy.Field()
    metadata_uri = scrapy.Field()
    twitter = scrapy.Field()
    telegram = scrapy.Field()
    bonding_curve = scrapy.Field()
    associated_bonding_curve = scrapy.Field()
    creator = scrapy.Field()
    created_timestamp = scrapy.Field()
    raydium_pool = scrapy.Field()
    complete = scrapy.Field()
    virtual_sol_reserves = scrapy.Field()
    virtual_token_reserves = scrapy.Field()
    hidden = scrapy.Field()
    total_supply = scrapy.Field()
    website = scrapy.Field()
    show_name = scrapy.Field()
    last_trade_timestamp = scrapy.Field()
    king_of_the_hill_timestamp = scrapy.Field()
    market_cap = scrapy.Field()
    reply_count = scrapy.Field()
    last_reply = scrapy.Field()
    nsfw = scrapy.Field()
    market_id = scrapy.Field()
    inverted = scrapy.Field()
    is_currently_live = scrapy.Field()
    username = scrapy.Field()
    profile_image = scrapy.Field()
    usd_market_cap = scrapy.Field()
