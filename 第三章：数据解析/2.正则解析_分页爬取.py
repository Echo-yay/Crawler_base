# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/12 15:01
#需求：分页爬取糗事百科中的糗图

import requests
import re
import os
if __name__ == '__main__':
    if not os.path.exists('./糗图libs'):
        os.mkdir('./糗图libs')

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    #设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d'
    pageNum = 2
    for pageNum in range(1,5):
        #对应页码的url
        new_url = format(url%pageNum)

        # 使用通用爬虫对整张页面进行爬取
        page_text = requests.get(url=new_url, headers=header).text
        #使用聚焦爬虫爬取图片
        #使用正则提取图片src
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        # 将正则作用到页面中
        # 将正则作用到数据解析中一定使用re.S
        img_src_list = re.findall(ex, page_text, re.S)  # re.S--单行匹配，re.M--多行匹配
        #print(img_src_list)
        for src in img_src_list:
            src = 'https:'+src
            image = requests.get(url=src,headers=header).content
            imgName = src.split('/')[-1]
            imgPath = './糗图libs/' + imgName
            with open(imgPath,'wb') as fp:
                fp.write(image)
            print(imgName,'下载成功！')



