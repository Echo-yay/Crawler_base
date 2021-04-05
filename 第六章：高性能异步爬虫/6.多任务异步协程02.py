# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/5 14:59
import requests
import asyncio
import time

start = time.time()
urls = [
    'http://127.0.0.1:5000/an',
    'http://127.0.0.1:5000/echo',
    'http://127.0.0.1:5000/tom'
]

async def get_page(url):
    print('正在下载',url)
    #requests.get是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    #aiohttp：基于异步网络请求的模块
    response = requests.get(url=url).text
    print('下载完毕',response)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print('总耗时：',end-start)