# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/12 13:50
#需求：爬取糗事百科中糗图板块下的所有糗图图片

import requests
import re
import os
if __name__ == '__main__':
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./糗图libs'):
        os.mkdir('./糗图libs')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    url = 'https://www.qiushibaike.com/imgrank'
    #使用通用爬虫对整张页面进行爬取
    page_text = requests.get(url=url,headers=header).text

    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    #将正则作用到页面中
    #将正则作用到数据解析中一定使用re.S
    img_src_list = re.findall(ex,page_text,re.S)   #re.S--单行匹配，re.M--多行匹配
    #print(img_src_list)
    for src in img_src_list:
        #拼接出一个完整的图片url
        src = 'https:'+src
        image_data = requests.get(url=src,headers=header).content
        #生成图片名称
        image_name = src.split('/')[-1]
        #图片最终存储路径
        imgPath = './糗图libs/'+image_name
        with open(imgPath,'wb') as fp:
            fp.write(image_data)
            print(image_name,'下载成功！')