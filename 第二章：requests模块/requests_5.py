# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/11 15:50
#肯德基店数量

import requests

if __name__ == '__main__':
    #指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    #UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    #发起请求keyword
    keyword = input('请输入查询城市：')
    param = {
        'cname':'',
        'pid':'',
        'keyword': keyword,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url,data=param,headers=header)

    #获取响应
    dict_text = response.text
    #存储
    filename = keyword+'.txt'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(dict_text)
    print('结束！')


