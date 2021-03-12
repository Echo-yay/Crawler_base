# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/11 14:28

#破解有道翻译
import requests
import json
if __name__ == '__main__':
    #指定url
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #UA伪装
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
    }
    #发起请求
    kw = input('请输入内容：')
    word = {
        'i':kw
    }
    response = requests.post(url=url,data=word,headers=header)
    #获取响应信息
    dict_obj = response.json()
    #存储
    filename=kw+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False)
    print('over!')


