# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/17 16:48

import requests
from lxml import etree

# 需求：爬取58二手房中的房源信息
if __name__ == '__main__':
    #爬取页面数据
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    count = 0   #房的总数
    url = 'https://sjz.58.com/xinjisjz/ershoufang/p%d/'
    page_num = 1
    for page_num in range(1,7):
        new_url = format(url%page_num)
        page_text = requests.get(url=new_url,headers=header).text
        #print(page_text)
        #break

        #数据接续
        tree = etree.HTML(page_text)
        title_list = tree.xpath('//section[@class="list"]//div[@class="property-content-title"]/h3/text()')
        #print(title_list)
        #break
        num = len(title_list)   #该页房套数
        count += num
        with open('二手房源.txt','a+',encoding='utf-8') as fp:
            for item in title_list:
                title = item
                fp.write(title)
                fp.write('\n')
            fp.write('共有{0}套房'.format(count))
    print('数据爬取完毕！')

