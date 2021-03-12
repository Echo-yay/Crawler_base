# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/12 11:51
#需求：爬取糗事百科中糗图板块模板下所有的糗图图片
#如何爬取图片

import requests
if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    url = 'http://pic.qiushibaike.com/system/pictures/12414/124140584/medium/Y9W3W1NCNNXLEPTW.jpg'
    #content返回的是二进制形式的图片数据
    #content（二进制）text(字符串)json(对象)
    image_data = requests.get(url=url,headers=header).content

    with open('./糗图.jpg','wb') as fp:   #wb以二进制方法写入
        fp.write(image_data)
