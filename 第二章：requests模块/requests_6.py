# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/11 16:25
#爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关详情数据
#动态加载出来的数据的爬取

import requests
import json
if __name__ == '__main__':
    #批量获取不同企业的ID值
    url_id = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    id_list = []  # 存储企业的id
    all_data_list = []  # 存储所有的企业详情数据
    #参数的封装
    for page in range(1,6):
        page = str(page)

        data_id = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }


        response = requests.post(url=url_id,data=data_id,headers=header)
        json_ids = response.json()

        #获取id
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        #print(id_list)

    #获取企业详情数据
    url_mess = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data_mess = {
            'id': id
        }

        respose_mess = requests.post(url=url_mess,data=data_mess,headers=header)
        message_json = respose_mess.json()
        #print(message)
        all_data_list.append(message_json)

    #存储
    fp = open('./化妆品详情.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!')


