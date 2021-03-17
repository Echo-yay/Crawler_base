# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/17 15:51

from lxml import etree

if __name__ == '__main__':
    #实例化etree对象，且将被解析的源码加载到该对象中
    '''
    tree = etree.parse('test.html')
    r = tree.xpath('/html/body/div')    #返回值类型是列表
    #报错：lxml.etree.XMLSyntaxError，原因是自己html代码书写不规范，不符合xml解析器的使用规范
    '''

    '''解决方法自己创建解析器，同时增加parser参数'''
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('test.html',parser=parser)
    #result = etree.tostring(tree)
    #r = tree.xpath('/html/body/div')    #返回值为列表，第一个'/'代表从根节点（目录）开始定位，一个/表示一个层级
    #print(r)
    #r_1 = tree.xpath('/html//div')  #//表示多个层级
    #print(r_1)
    #r_2 = tree.xpath('//div')  # //表示从任意位置开始定位
    #print(r_2)
    #r = tree.xpath('//div[@class="song"]')
    # print(r)
    #r = tree.xpath('//div[@class="song"]/p[3]') #索引是从1开始的
    #print(r)
    #r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')  #返回值类型为列表：['杜牧']
    #e = r[0]
    #print(e)    #杜牧
    #r = tree.xpath('//div[@class="tang"]//li[7]//text()')
    #print(r)
    #r = tree.xpath('//div[@class="tang"]//text()')
    #print(r)
    r = tree.xpath('//div[@class="song"]/img/@src')
    print(r)