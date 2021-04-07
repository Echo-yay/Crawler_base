# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/7 12:55
from selenium import webdriver
from time import sleep
#导入动作链对应的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

#如果定位的标签是存在于iframe中的，则必须通过如下操作才能进行标签定位
bro.switch_to.frame('iframeResult') #切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')
#print(div)

#拖动标签（动作链）
action = ActionChains(bro)
#点击且长按指定标签
action.click_and_hold(div)

for i in range(5):
    #perfrom()立即执行动作链操作
    action.move_by_offset(17,0).perform()
    sleep(0.3)

#释放动作链
action.release()

bro.quit()
