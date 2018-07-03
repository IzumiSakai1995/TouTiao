#__author: Liu Zheng
#date:2018/6/30

from urllib.parse import urlencode
import time
import re
import json
import requests
def get_index_page(offset,keyword):
    data = {
        'offset': 'offset',
        'format': 'json',
        'keyword': 'keyword',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    response = requests.get(url)
    return response.text
def parse_index_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():  #dict.keys()返回一个字典的所有键名
        for item in data.get('data'): #dict.get(key,default=None) 返回指定键的值，字典中不存在则返回None
            yield item.get('article_url')
def main():
    html = get_index_page(0,'街拍')
    for url in parse_index_page(html):
        print(url)


if __name__ == '__main__':
    main()