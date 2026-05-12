from cachetools import TTLCache

recommendation_cache = TTLCache(maxsize=1000, ttl=300)