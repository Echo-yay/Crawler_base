# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/25 13:30

# 需求；解析出所有城市名称 https://www.aqistudy.cn/historydata/
'''ctrl+？全部注释'''

import requests
from lxml import etree

if __name__ == '__main__':

    '''解析了两次分别得到热门城市和全部城市'''
    #
    # all_city_list = []  #存储获取的全部城市名
    # hot_city_list = []  #存储热门城市名
    # # UA伪装
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36'
    # }
    # # 请求url
    # url = 'https://www.aqistudy.cn/historydata/'
    # # 获取响应数据
    # page_text = requests.get(url=url,headers=headers).text
    # #print(page_text)
    #
    # # 实例化etree对象，并将页面信息加载到对象中
    # tree = etree.HTML(page_text)
    # # 定位城市信息
    # # 全部城市
    # all_city_li = tree.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li')
    # for li in all_city_li:
    #     cityName = li.xpath('./a/text()')
    #     all_city_list.append(cityName[0])
    # #print(all_city_list)
    # # 热门城市
    # hot_city_li = tree.xpath('//div[@class="hot"]/div//li')
    # for li in hot_city_li:
    #     cityName = li.xpath('./a/text()')
    #     hot_city_list.append(cityName[0])
    # #print(hot_city_list)
    #
    # # 持久化存储
    # with open('城市名.txt','w',encoding='utf-8') as fp:
    #     fp.write('热门城市：\n')
    #     for city in hot_city_list:
    #         fp.write(city)
    #         fp.write('\n')
    #     fp.write('-----------------------------------\n')
    #     fp.write('全部城市：\n')
    #     for city in all_city_list:
    #         fp.write(city)
    #         fp.write('\n')
    #
    # print('爬取成功！')

    '''解析一次得到所有城市和热门城市的a标签'''

    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36'
    }
    # 请求url
    url = 'https://www.aqistudy.cn/historydata/'
     # 获取响应数据
    page_text = requests.get(url=url,headers=headers).text
    #print(page_text)

    # 实例化etree对象，并将页面信息加载到对象中
    tree = etree.HTML(page_text)

    # 解析城市标签
    # div[@class="bottom"]/ul/li/a           热门城市
    # div[@class="bottom"]/ul/div[2]/li/a    全部城市
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_name = []
    for a in a_list:
        cityName = a.xpath('./text()')[0]
        all_city_name.append(cityName)
    print(all_city_name)

