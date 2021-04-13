# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XiaohuaproPipeline:
    fp = None
    def open_spider(self,spider):
        print('开始爬取数据......')
        self.fp = open('./图片名称.txt','w',encoding='utf-8')
        self.fp.write('图片名称：')

    def process_item(self, item, spider):
        img_name = item['img_name']
        self.fp.write('\n'+img_name)
        return item

    def close_spider(self,spider):
        print('数据爬取结束！')
        self.fp.close()


'''
问题：
错误为代码：
AttributeError: ‘NoneType’ object has no attribute ‘write’
fp的布尔值属性没变，还是None，所以不能写，后面还有个不能close，都是一个意思。
错误原因：重写父类时候自己定义的start_spider方法和end_spider方法并没有被调用，因为人家只能调用固定的方法……还以为可以自定义的，所以报错了。
————————————————
版权声明：本文为CSDN博主「四如君」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44699828/article/details/108189947
'''