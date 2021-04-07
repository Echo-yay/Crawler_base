# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/7 16:24

from lxml import etree
from selenium import webdriver

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
url = 'https://ishare.ifeng.com/mediaShare/home/702/media?aman=efV2bdd6027bb2Uc5bm3bf7824me894710y024cffc'
bro.get(url)
page = bro.page_source
#print(page)
tree = etree.HTML(page)
div_list = tree.xpath('//*[@id="root"]/div[1]/div[4]/div[1]/div')
for div in div_list:
    src = div.xpath('.//a/text()')
    print(src)
