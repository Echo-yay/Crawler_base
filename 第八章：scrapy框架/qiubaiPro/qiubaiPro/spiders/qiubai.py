import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    '''基于终端指令存储'''
    # def parse(self, response):
    #     #解析：作者的名称+段子的内容
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     #print(div_list)
    #     all_data = []   #存储所有解析到的数据
    #     for div in div_list:
    #         #xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         #extract可以将Selector对象中data参数存储的字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取出来
    #         content1 = div.xpath('./a/div/span/text()').extract()
    #         #将content中的元素连接成一个字符串
    #         content2 = ''.join(content1)
    #         # print(author)
    #         # print(content1)
    #         # print(content2)
    #         # break
    #
    #         dic = {
    #             'author':author,
    #             'content':content2
    #         }
    #         all_data.append(dic)
    #
    #     return all_data

    def parse(self, response):
        # 解析：作者的名称+段子的内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        # print(div_list)

        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取出来
            content1 = div.xpath('./a[1]/div/span/text()').extract()
            # 将content中的元素连接成一个字符串
            content2 = ''.join(content1)

            #将解析的数据封装存储到item类型的对象中
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content2

            #将item类型的对象提交给管道进行持久化存储的操作
            yield item



