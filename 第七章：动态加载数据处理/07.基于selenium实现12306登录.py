# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/7 19:11

#需求：登录12306：滑块验证待解决

from CodeClass import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep
from PIL import Image
from selenium.webdriver import ActionChains

#使用selenium打开页面
#实现selenium规避被检测到的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe',options=option)
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
#窗口最大化
#bro.maximize_window()

#print(bro.page_source)
#sleep(1)

login_tag = bro.find_element_by_link_text('账号登录')
login_tag.click()

username_tag = bro.find_element_by_id('J-userName')
password_tag = bro.find_element_by_id('J-password')
username_tag.send_keys('15633250136')
password_tag.send_keys('1111111')

bro.execute_script('document.body.style.zoom="0.5"')
#save_screenshot()截图并保存
bro.save_screenshot('./a.png')

#确定验证码图片对应的左上角和右下角的坐标（裁剪的区域确定）
'''位置发生偏移解决方案   https://www.cnblogs.com/jiyu-hlzy/p/12155738.html'''

code_img_ele = bro.find_elements_by_class_name('imgCode')[0]
#print(code_img_ele)
location = code_img_ele.location    #验证码图片左上角的坐标x,y
print('location:',location)
size = code_img_ele.size    #验证码标签对应的长和宽
print('size:',size)
#左上角和右下角坐标
rangle = (
    int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])
)
print(rangle)
'''至此验证码图片区域确定'''

#裁剪验证码区域
#实例化Image对象
i = Image.open('./a.png')
code_img_name = './code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)

#因为显示偏移导致截图时调整了页面，在截图操作之后还需要将页面调回，否则定位不到原位置
bro.execute_script('document.body.style.zoom="1"')

#识别图片
chaojiying = Chaojiying_Client('Echoyay', '0822CNTTge', '914431')  # 用户中心>>软件ID 生成一个替换 96001
im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
result = chaojiying.PostPic(im, 9004)['pic_str']
print('result:',result)
all_list = []   #要存储即将被点击的点的坐标，存储形式  [[x1,y1],[x2,y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)

print(all_list)

#遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    #move_to_element_with_offset()将参照物转到code图片上
    action = ActionChains(bro)
    action.move_to_element_with_offset(code_img_ele,x,y).click().perform()
    sleep(0.5)

login_btn = bro.find_element_by_link_text('立即登录')
login_btn.click()
sleep(3)
bro.quit()



