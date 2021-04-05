# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/30 12:31

#单线程下的串行数据爬取
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
urls = [
    'http://down.gerenjianli.com/mb2018/jianli_moban_839249.doc',
    'http://down.gerenjianli.com/mb2018/jianli_moban_394675.doc',
    'http://down.gerenjianli.com/mb2018/jianli_moban_825705.docx',
]

def get_conent(url):
    print('正在爬取：',url)
    #get方法是一个阻塞的方法/函数
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        return response.content

def parse_content(content):
    print('响应数据的长度为：',len(content))

for url in urls:
    content = get_conent(url)
    parse_content(content)