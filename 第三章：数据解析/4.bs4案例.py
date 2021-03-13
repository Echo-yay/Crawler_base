# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/13 16:19

#需求：爬取三国演义小说所有的章节标题和内容

import os
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    filename = '三国演义.txt'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    #爬取整张页面
    page = requests.get(url=url,headers=header)
    #解决网页乱码
    page.encoding = 'utf-8'
    page_text = page.text
    #在首页中解析出章节标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    all_list = soup.select('.book-mulu a')
    len = len(all_list)
    for i in range(len):
        #获取章节标题
        sub_title = all_list[i].text
        #获取章节内容的url
        cont_href = all_list[i]['href']
        cont_href = 'https://www.shicimingju.com'+cont_href
        #print(cont_href)

        #对章节内容发起url请求
        content_page = requests.get(url=cont_href,headers=header)
        content_page.encoding = 'utf-8'
        content_page_text = content_page.text

        content_soup = BeautifulSoup(content_page_text,'lxml')
        #print(content_soup)
        #break
        content = content_soup.find('div',class_="chapter_content").text
        #print(content)

        with open(filename,'a+',encoding='utf-8') as fp:
            fp.write(sub_title)
            fp.write(content)
            fp.write('\n')

        print('第',i+1,'章录入完毕！')
    print('三国演义录入完毕！')

