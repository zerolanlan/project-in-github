import json

def response(flow):
    url = 'product.mapi.dangdang.com'
    page_size = 'page_size=15'
    # 对url进行筛选,只选取评论的url
    if url and page_size in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        for item in data['review_list']:
            # 获取用户昵称
            if len(item['cust_name']) > 0:
                name = item['cust_name']
            else:
                name = '无名'
            print(item['cust_name'])
            # 获取用户评分
            if len(item['score']) > 0:
                score = str(item['score'])
            else:
                score = '0'
            print(item['score'] + '\n')
            # 获取用户评论
            content = item['content'].replace(',', '，').replace('\n', '')
            print(item['content'] + '\n')
            # 获取用户评论时间
            creation_date = item['creation_date']
            print(item['creation_date'])
            # 获取有用数
            if len(str(item['total_helpful_num'])) > 0 :
                total_helpful_num = str(item['total_helpful_num'])
            else:
                total_helpful_num = '0'
            print(item['total_helpful_num'])
            # 获取无用数
            if len(str(item['total_useless_num'])) > 0 :
                total_useless_num = str(item['total_useless_num'])
            else:
                total_useless_num = '0'
            print(item['total_useless_num'])
            # 获取评论数
            if len(str(item['total_reply_num'])) > 0 :
                total_reply_num = str(item['total_reply_num'])
            else:
                total_reply_num = '0'
            print(item['total_reply_num'])
            print('\n')
            # 将获取信息写入csv文件
            with open('alive.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(name + ',' + score + ',' + content + ',' + creation_date + ',' + total_helpful_num + ',' + total_useless_num + ',' + total_reply_num + '\n')
