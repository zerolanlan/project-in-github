  import json
 
import pymysql
import requests
 
end_page = int(input('请输入结束页面：'))
keyword = input('请输入查找关键字：')
 
 
def get_url():
    for page in range(end_page):
        offset = (page-1) * 20
        url = 'https://www.toutiao.com/search_content/?'
        params = {
            'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
            'from': 'search_tab'
        }
        headers = {
            'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        try:
            toutiao_json = requests.get(url, params=params, headers=headers).text
            return toutiao_json
        except:
            return None
 
 
def get_toutiao(toutiao_json):
 
    json_toutiao = json.loads(toutiao_json)
    data_list = json_toutiao['data']
    items = []
    for data in data_list:
        if data.get('title'):
            title = data.get('title')
            images = data.get('image_list')
            url_list = []
            for image in images:
                url = 'https:' + image['url']
                url_list.append(url)
            dict1 = {
                'title': title,
                'image': url_list
            }
            items.append(dict1)
    return items
 
 
def save_content(items):
    filename = keyword + '.txt'
    for item in items:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False))
 
 
def main():
    toutiao_json = get_url()
    items = get_toutiao(toutiao_json)
    save_content(items)
 
 
if __name__ == '__main__':
    main()
 
