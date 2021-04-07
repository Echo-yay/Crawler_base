# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/7 18:32

from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com/')
#切换作用域
bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()
sleep(1)
username_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
username_tag.send_keys('1740636835')
sleep(1)
password_tag.send_keys('0822CNTTge.1997')
sleep(1)

login_btn = bro.find_element_by_id('login_button')
login_btn.click()
sleep(3)
bro.quit()