# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/5 15:16

#环境的安装：pip install aiohttp
#使用该模块中的ClientSession

import requests
import asyncio
import time
import aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/an',
    'http://127.0.0.1:5000/echo',
    'http://127.0.0.1:5000/tom'
]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers（UA伪装），params/data（参数），proxy='http://ip:port'（代理IP）
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read()返回的是二进制形式的响应数据
            #json()返回的是json对象

            #注意：在获取响应数据操作之前一定要使用await进行手动挂起
            page_text =await response.text()
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print('总耗时：',end-start)