# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/10 16:21
# 爬取搜狗首页的页面数据
import requests
if __name__ == '__main__':
    # 指定url
    url = 'http://ww.sogou.com/'
    # 发起请求
    response = requests.get(url=url)  #get方法会返回一个响应对象
    # 获取响应数据,text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')
