# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/18 15:16

#需求：解析下载图片数据  http://pic.netbian.com/4kbeijing/
import requests
from lxml import etree
import os

if __name__ == '__main__':
    if not os.path.exists('./4k图片'):
        os.mkdir('./4k图片')

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    url = 'https://pic.netbian.com/4kbeijing/'
    # 指定url
    # 发起请求并获取页面数据
    page_text = requests.get(url=url,headers=header).text
    #print(page_text)

    # 初始化etree对象，并将页面数据加载到etree对象中
    tree = etree.HTML(page_text)
    #print(tree)

    # 定位图片位置
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    #print(img_url_list)
    for li in li_list:
        #获取图片地址
        imgURL = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        imgName = li.xpath('./a/img/@alt')[0]+'.jpg'
        #通常处理中文乱码的解决方案
        imgName = imgName.encode('iso-8859-1').decode('gbk')
        print(imgURL)
        print(imgName)

        image_data = requests.get(url=imgURL, headers=header).content
        #持久化存储
        imgPath = './4k图片/'+imgName
        with open(imgPath,'wb') as fp:
            fp.write(image_data)
    print('爬取结束！')

'''
问题为：Image not load
原因：得到图片src之后没有将其作为url请求，而是使用的最开始的url
'''

