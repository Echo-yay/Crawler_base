import scrapy
from xiaohuaPro.items import XiaohuaproItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/ziliao/neidi/index.html']

    #生成一个通用的url模板(不可变)
    url = 'http://www.521609.com/ziliao/neidi/index_%d.html'
    page_num = 2

    #基于start_url进行数据解析的操作
    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div[2]/ul/li')
        #print(li_list)
        for li in li_list:
            img_name = li.xpath('./a[2]/h3/text()').extract_first()
            print(img_name)
            item = XiaohuaproItem()
            item['img_name'] = img_name
            yield item

        if self.page_num <= 66:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            #手动请求:callback回调函数专门用作数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)

