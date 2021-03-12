# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/10 16:41

# 爬取搜狗指定词条对应的搜索结果页面
# UA---User-Agent 请求载体的身份标识
'''
UA检测
    门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求载体身份标识为某一浏览器，说明是正常请求；
    如果监测到请求载体标识不是某一浏览器，则表示该请求为不正常的请求（爬虫），则服务器端有可能拒绝请求
UA伪装
    让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''
import requests
if __name__ == '__main__':
    #1.指定url
    url = 'https://www.sogou.com/web?query=%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8'    #query后为搜索关键词
    #2.UA伪装：将对应的User-Agent封装到一个字典中。User-Agent的值为抓取的某一浏览器的User-Agent
    headers = {
        'User-Agent':'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.182Safari / 537.36'
    }
    #3.处理url携带的参数（动态）：封装到字典中
    kw = input('录入关键词：')
    param = {
        'query':kw
    }
    #4.对指定的url发起的请求对应url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    #5.获取响应数据
    page_text = response.text
    #6.存储
    filename = kw + '.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'保存成功！')
