# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/10 17:13

#破解百度翻译(使用Ajax)
'''Ajax是一项用于网站开发的重要技术。可以在不刷新网页的情况下，与服务端交互。'''
#选择“XHR”，显示的是Ajax请求的数据包

import requests
import json

if __name__ == '__main__':
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2.UA伪装
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.182Safari / 537.36'
    }
    #3.post请求参数处理（同get一致）
    kw = input('请输入要翻译的内容：')
    data={
        'kw':kw
    }
    #4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5.获取响应数据;json()方法返回的是obj（如果确认响应数据是json类型，才可以用json；查看响应数据类型的方法为：点击数据包，寻找Response-Header中的Content-Type）
    dict_obj = response.json()
    print(dict_obj)
    #6.持久化存储
    filename = kw+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False)    #将python中的对象转化成json储存到文件中
    fp.close()
    print('爬取结束！')

