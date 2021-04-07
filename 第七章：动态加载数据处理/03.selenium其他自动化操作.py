# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/5 16:28

from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com/')

#在指定搜索框录入关键词
#定位搜索框
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('森系连衣裙')

#滚轮
#向下拖动 在开发者工具中-->console中执行一组json代码
#执行一组js程序
#(0,document.body.scrollHeight)表示向左不动，向下滚动一屏
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

#点击搜索按钮
button = bro.find_element_by_css_selector('.btn-search')
#button = bro.find_element_by_class_name('btn-search')
button.click()

bro.get('http://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()

sleep(5)
bro.quit()


