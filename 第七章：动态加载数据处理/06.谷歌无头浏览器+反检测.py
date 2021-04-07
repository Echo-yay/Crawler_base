# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/7 18:54

from selenium import webdriver
from time import sleep
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实例化Options对象，用来实现无界面模式打开chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#实现selenium规避被检测到的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)

#无可视化界面（无头浏览器）  phantomJs
bro.get('https://www.baidu.com')
print(bro.page_source)
sleep(2)
bro.quit()