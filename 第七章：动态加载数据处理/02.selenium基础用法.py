# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/5 16:12

from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path='./chromedriver.exe')

#获取药监总局化妆品的详情
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

#获取浏览器当前页面的源码数据
page_text = bro.page_source

#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(4)
bro.quit()