# 导入所需模块
import requests
import os
import re
import sys
import time
from urllib import request, error
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def change(nstr):  # 把bs4字符串转成Unicode字符串
    ustr = ''
    ustr = ustr.join(nstr)
    return ustr

def tuichu(user_in):  # 快速退出软件（没啥用）
    if user_in.lower() == 'exit' or user_in == '0':
        sys.exit()

def makedirs(dir_name):  # 创建目录
    if os.path.isdir(dir_name) == False:
        os.makedirs(dir_name)

def search_req(url):  # 搜索请求（含错误捕获）
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.ConnectTimeout:
        print('[!]请求超时！正在尝试重连！')
        i = 1
        while i < 4: # 超时重连
            try:
                response = requests.get(url, timeout=5).text
                return response
            except requests.exceptions.RequestException:
                if i==3: 
                    print('[!]第 3 次重连失败,程序将在 3 秒后退出！')
                else:
                    print('[!]第 '+str(i)+' 次重连失败，正在尝试重连！')
                i += 1
        time.sleep(3)
        sys.exit()
    except requests.HTTPError:
        print('[!]请求失败！程序将于 3 秒后退出！')
        time.sleep(3)
        sys.exit()

def download(url, path):  # 下载图片(含错误捕获)
    try:
        opener = request.build_opener()
        opener.addheaders = [('User-agent', UserAgent().random)] #下载图片添加User-Agent池
        request.install_opener(opener)
        request.urlretrieve(url, path)
    except error.HTTPError as e:
        print('[!]下载发生错误：'+e.reason)
    except error.URLError as e:
        print('[!]下载发生错误：'+e.reason)

print('[#] 欢迎使用美图录Crawler[version:0.1,2020.02.10]！\n    前往数据源：https://www.meitulu.com 下载更多精彩图片！\n    图片存储位置：桌面。出现[>]时键入 0 或 exit 退出程序。建议单次不要爬太多，会被封IP的。\n')
# 获取搜索结果
while True:
    keyword = input('[>] 请输入搜索关键词： ')
    tuichu(keyword)
    t1 = time.time()
    api = 'https://www.meitulu.com/search/'+keyword
    html = search_req(api)
    soup = BeautifulSoup(html, 'lxml')
    img_cons = soup.find(name='div', attrs={'class': 'boxs'}).contents[1].contents
    for img_con in img_cons:
        if img_con == '\n':
            img_cons.remove(img_con)
    t2 = time.time()
    if len(img_cons) != 0:
        print('[#] 共找到匹配结果 '+str(len(img_cons)) +
              ' 条,耗时 '+str(round(t2-t1, 3))+' 秒')
        break
    else:
        print('[!] 没有找到匹配结果，换个关键词试试吧！')
# 用户输入：要爬几个图册
while True:
    n = input('[>] 请输入需要爬取的结果数'+'(不超过匹配结果 '+str(len(img_cons))+')： ')
    tuichu(n)
    if n.isdecimal() == True:
        if int(n) <= len(img_cons):
            n = int(n)
            break
    print('[!] 您的输入非法，请重新输入！')

results = {}  # 存放所有图册标题和链接
# 解析每个图册
for img_con in img_cons[:n]:
    str_alt = change(img_con.a.img['alt'])  # 图册标题
    str_src = change(img_con.a.img['src'])  # 封面图链接
    str_num = change(img_con.p.contents[1])
    num = re.search(r'(?<=：).*(?=张)', str_num).group().strip()  # 图片数量
    links = []  # 存放每个图册的所有链接
    for i in range(1, int(num)+1):  # 生成链接
        link = str_src.replace('0.jpg', '')+str(i)+'.jpg'
        links.append(link)
    results[str_alt] = links  # 这里把图册标题和对应链接储存到字典中，方便后面一个图册建一个文件夹
# 下载图片
path = 'C://Users/lx223/Desktop/图虫/'  # 默认保存路径
img_count = 0  # 下载图片计数
col_count = 1  # 下载图册计数
print('--------------------Started--------------------\n')
t3 = time.time()
for name, urls in results.items():
    print('<'+str(col_count)+'/'+str(n)+'> '+'正在下载图集 ★ '+name)
    makedirs(path+name+'\\')
    for i in range(len(urls)):
        path1 = path+name+'\\'+str(i+1)+'.jpg'
        if os.path.isfile(path1) == False:
            print('    >>正在下载第 '+str(i+1)+' 张，还剩 '+str(len(urls)-i-1)+' 张')
            download(urls[i], path1)
        else:
            print('    --第 '+str(i+1)+' 张已存在，还剩 '+str(len(urls)-i-1)+' 张')   
    print('<'+str(col_count)+'/'+str(n)+'> '+'成功下载 ★ '+name)
    img_count += len(urls)
    col_count += 1
t4 = time.time()
print('\n---------------------Done---------------------')
print('[#] 已完成下载任务.共爬取图片 '+str(img_count)+' 张,耗时 '+str(round(t4-t3, 3))+' 秒')
input('请按[Enter]键退出...')