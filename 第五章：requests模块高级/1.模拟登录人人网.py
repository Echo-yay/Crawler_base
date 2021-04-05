# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/26 16:11

#编码流程
# 1.验证码识别，获取验证码图片的文字数据
# 2.发起POST请求（处理请求参数）
# 3.对响应数据进行持久化存储

import requests
from lxml import etree
from CodeClass import Chaojiying_Client

#封装识别验证码图片的函数
def getCodeText(filename,codeType):
    chaojiying = Chaojiying_Client('Echoyay', '0822CNTTge', '914431')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(filename, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, codeType)

#1.对验证码图片进行捕获和识别
url = 'http://www.renren.com/SysHome.do'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//dl[@id="codeimg"]//img/@src')[0]
#print(code_img_src)
code_img_data = requests.get(url=code_img_src,headers=headers).content
with open('code.jpg','wb') as fp:
    fp.write(code_img_data)

#使用超级鹰平台对验证码进行识别
code_info = dict()
code_info = getCodeText('code.jpg','1902')
code = code_info['pic_str']
print(code)

#post请求的发送(模拟登录)
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021201647386'
data = {
    'email': '15633250136',
    'icode': code,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': 1,
    'captcha_type': 'web_login',
    'password': '6bd227223f20028107ec4a9ea32263f9d0169ec586cd8a73e8ec3a51fb7cd581',
    'rkey': 'fadff523aaff6e83227ac1509d88c752',
    'f': '',
}
response = requests.post(url=login_url,data=data,headers=headers)
login_page_text = response.text
print(response.status_code)    #响应状态码，状态码是200表示模拟登录成功
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(login_page_text)