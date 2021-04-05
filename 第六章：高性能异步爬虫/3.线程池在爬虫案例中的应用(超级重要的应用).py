# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/31 13:42

#需求：爬取梨视频的视频数据

#原则：线程池处理的是阻塞且耗时的操作
import requests
from lxml import etree
import os
from multiprocessing.dummy import Pool

if not os.path.exists('./梨视频'):
    os.mkdir('./梨视频')

#向梨视频发起请求
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

url = 'https://www.pearvideo.com/category_4'

page_text = requests.get(url=url,headers=headers).text
#print(page_text)

#解析详情页的url和名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
#print(li_list)

urls = []   #存储所有视频的链接和名字
for li in li_list:
    #在li标签中进行局部数据的解析
    '''detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]'''
    video_id = li.xpath('./div/a/@href')[0].split('_')[1]
    detail_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=%s' %video_id

    #print(detail_url)
    #break
    detail_name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    #print(detail_name)
    #break

    headers= {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Referer':'https: // www.pearvideo.com / video_%s' %video_id,
    }
    detail_page = requests.get(url=detail_url,headers=headers).json()
    #print(detail_page)
    '''更换detail_url后，得到如下信息：
    {
	"resultCode":"5",
	"resultMsg":"该文章已经下线！",
	"systemTime": "1617172365809"
    }
    证明梨视频采取了反爬机制。
    对比不同方式进入该页的请求头文件发现正常请求时头部多了参数：Referer: https://www.pearvideo.com/video_1724978
    解决方式：在头文件中加入即可，第43行
    '''

    '''添加参数后得到正常数据
    {
	"resultCode":"1",
	"resultMsg":"success", "reqId":"6e2689a0-5387-4c35-84ac-35f23c53b3e4",
	"systemTime": "1617172761528",
	"videoInfo":{"playSta":"1","video_image":"https://image1.pearvideo.com/cont/20210330/10887340-155031-1.png","videos":{"hdUrl":"","hdflvUrl":"","sdUrl":"","sdflvUrl":"","srcUrl":"https://video.pearvideo.com/mp4/third/20210330/1617172761528-10887340-154044-hd.mp4"}}
    }
    '''
    #break
    #detail_tree = etree.HTML(detail_page)
    #video = detail_tree.xpath('//div[@class="img prism-player play"]/video/@src')
    #print(video)    #得到[]，发现video是动态加载出来的(ajex)，所以应该将访问的网址改为动态加载的包的网址,33行
    #break
    videoUrl = detail_page['videoInfo']['videos']['srcUrl']
    #print(videoUrl)
    '''
    结果为此网址
    https://video.pearvideo.com/mp4/third/20210330/1617173236852-10887340-154044-hd.mp4
    打不开视频网页
    正确网址为：
    https://video.pearvideo.com/mp4/third/20210330/cont-1724978-10887340-154044-hd.mp4
    '1617173236852'应该替换为'cont-video_id'
    '''

    #print(video_id)
    # videoUrl.split('/')[-1].split('-')[0]将不同部分取出来
    videoUrl = videoUrl.replace(videoUrl.split('/')[-1].split('-')[0],'cont-%s' %video_id)
    #print(videoUrl)
    dic = {
        'name':detail_name,
        'url':videoUrl
    }
    urls.append(dic)
print(urls)

def get_video_data(dic):
    url = dic['url']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    print('该视频正在下载...')
    video_data = requests.get(url=url,headers=headers).content
    #持久化存储
    with open('./梨视频/'+dic['name'],'wb') as fp:
        fp.write(video_data)
        print(dic['name']+'保存成功！')
#使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data,urls)
#关闭线程池
pool.close()
pool.join()

