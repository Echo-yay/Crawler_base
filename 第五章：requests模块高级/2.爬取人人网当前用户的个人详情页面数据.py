# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/28 16:55

import requests
from lxml import etree
from CodeClass import Chaojiying_Client

#封装识别验证码图片的函数
def getCodeText(filename,codeType):
    chaojiying = Chaojiying_Client('Echoyay', '0822CNTTge', '914431')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(filename, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, codeType)
#创建一个session对象
session = requests.Session()

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
#使用session进行post请求的发送
response = session.post(url=login_url,data=data,headers=headers)
login_page_text = response.text
print(response.status_code)    #响应状态码，状态码是200表示模拟登录成功

#爬取当前用户的个人主页对应的页面数据
detail_url = 'http://www.renren.com/976474165/profile'  #再登录之后再访问主页，但是服务器端不会已经登录请求的状态
#手动cookie处理
'''headers = {
    'Cookie':'anonymid=kmpzk4jk7fl77t; depovince=GW; _r01_=1; taihe_bi_sdk_uid=47b2bc156088b00d17269f9ac37a76f6; __utma=151146938.1221224632.1616744359.1616744359.1616744359.1; __utmz=151146938.1616744359.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ln_uact=15633250136; _de=59BACAF5B89F4DF098B641D1F469956B; jebecookies=a5b9a543-e953-45c0-8f35-9973de211c72|||||; JSESSIONID=abcdT1rbK0d2H4uRmK8Hx; ick_login=30626c78-43ef-44e6-bf1b-4547445d19f1; taihe_bi_sdk_session=4b40e53712e31c3871001707f901cb87; p=633f3319f4cd329e664914b1df6d74475; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20210328/1640/main_NIWk_0ab800005058195a.jpg; t=3cab2326444171079574cb50f01d16715; societyguester=3cab2326444171079574cb50f01d16715; id=976474165; xnsid=836f0f26; ver=7.0; loginfrom=null; wp_fold=0'
}'''
#使用携带cookie的session进行get请求的发送
detail_response  = session.get(url=detail_url,headers=headers)
detail_page_text = detail_response.text
print(detail_response.status_code)
with open('detail.html','w',encoding='utf-8') as fp:
    fp.write(detail_page_text)