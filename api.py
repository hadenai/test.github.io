import requests
KEY = '98240ab4-791e-43d7-a1c0-693b49fa6426'

CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
url = CONFIG_PATTERN.format(key=KEY)

r = requests.get(url)
config = r.json()


base_url = config['images']['base_url']
sizes = config['images']['poster_sizes']
"""
    'sizes' should be sorted in ascending order, so
        max_size = sizes[-1]
    should get the largest size as well.        
"""

def size_str_to_int(x):
    return float("inf") if x == 'original' else int(x[1:])
max_size = max(sizes, key=size_str_to_int)