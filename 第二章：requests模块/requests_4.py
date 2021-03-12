# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/11 15:25
#爬取豆瓣电影分类榜
import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '1',  #从库中第几部电影取
        'limit': '20',  #一次取出的个数
    }

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    response = requests.get(url=url,params=param,headers=header)

    list_data = response.json()
    fp = open('./豆瓣.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!')

