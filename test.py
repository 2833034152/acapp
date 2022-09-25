#from django.conf import settings
#settings.configure()
from django.core.cache import cache
cache.set('key1','good day!')
cache.set('key2','other day!')
print(cache.get('key1'))
print(cache.get('key2'))
