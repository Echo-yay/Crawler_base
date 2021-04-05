# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/31 13:03

#使用单线程串行方式运行
'''import time
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载成功：',str)

name_list = ['aa','bb','cc','dd']

start_time = time.time()

for i in range(len(name_list)):
    get_page(name_list[i])

end_time = time.time()
print('%d second'% (end_time-start_time))'''


#使用线程池的方式
import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
start_time = time.time()
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载成功：',str)

name_list = ['aa','bb','cc','dd']

#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理。map若有返回值，一定是个列表
pool.map(get_page,name_list)
end_time = time.time()
print(end_time-start_time)