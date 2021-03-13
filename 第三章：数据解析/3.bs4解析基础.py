# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/12 16:23
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #将本地的HTML文档中的数据加载到该对象中
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml') #html源码数据
    #print(soup)
    #print(soup.a)   #soup.tagName 返回的是第一次出现的该标签
    #print(soup.div)
    #print(soup.find("div")) #等同于soup.tagName
    #print(soup.find('div',class_='song'))
    #print(soup.find_all('a'))   #返回符合要求的所有标签，返回值类型是列表
    #print(soup.select('.tang'))
    #print(soup.select('.tang > ul > li > a')[0])
    #print(soup.select('.tang > ul a')[0].text)
    #print(soup.select('.tang a')[0].string)
    #print(soup.select('.tang a')[0].get_text())
    #print(soup.find('div',class_='tang').get_text())
    #print(soup.find('div',class_='song').string)
    print(soup.select('.tang a')[0]['href'])
