import os
from dotenv import load_dotenv
from flask_caching import Cache

load_dotenv()

config = {
    'CACHE_DEFAULT_TIMEOUT': os.getenv('CACHE_DEFAULT_TIMEOUT'),
    'CACHE_TYPE': os.getenv('CACHE_TYPE'),
    'CACHE_REDIS_PORT': os.getenv('CACHE_REDIS_PORT'),
    'CACHE_REDIS_URL': os.getenv('CACHE_REDIS_URL'),
    'CACHE_REDIS_HOST': os.getenv('CACHE_REDIS_HOST'),
}

cache = Cache(config=config)

def init_app(app):
    cache.init_app(app)
