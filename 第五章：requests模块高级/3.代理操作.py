# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/30 11:40

#需求：

import requests
url = 'https://www.baidu.com/s?wd=IP'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

page_text = requests.get(url=url,headers=headers,proxies={'https':'121.20.48.98:37859'}).text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

#反爬机制：封IP
#反反爬机制：使用代理进行请求发送
