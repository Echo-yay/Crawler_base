# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/25 15:40

# 需求：古诗文网验证码识别
import requests
from lxml import etree
from CodeClass import Chaojiying_Client

#封装识别验证码的函数
def getCodeText(filename,codeType):
    chaojiying = Chaojiying_Client('Echoyay', '0822CNTTge', '914431')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(filename, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, codeType)


headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36'
}
url = 'https://so.gushiwen.org/user/login.aspx/'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
img_src ='https://so.gushiwen.cn'+tree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')[0]
#print(img_src)
img = requests.get(url=img_src,headers=headers).content
filename = '验证码.jpg'
with open(filename,'wb') as fp:
    fp.write(img)
print('验证码已保存')

#调用打码平台的示例程序进行验证码图片数据识别
#print(getCodeText(filename,1902),type(getCodeText(filename,1902)))
codeInfo = dict()
codeInfo = getCodeText(filename,1902)
print('识别结果为：'+codeInfo['pic_str'])

