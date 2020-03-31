#2.0版本采用正则表达式匹配图片地址中的链接

import re  #正则表达式库
import time
import os 
from urllib import request

n=input('请输入你想爬取图片的网站：')
url_response=request.urlopen(n)  #打开链接
data=url_response.read().decode('utf-8')  # decode 以指定的编码格式解码字符串 data为编码后的源码
#ignore是在出现无法解码的字符时降低decode第二个参数error严格要求  可以不要，容易乱码
#data=url_response.read().decode('utf-8',"ignore")   中文乱码时utf-8换成gbk

#强大的google浏览器可以右键直接查看网页源码
#f = open('C://Users/lx223/Desktop/几套图.html','w+')  #把网页源码爬下来分析正则表达式
#f.write(data)  

#利用正则表达式找到所有符合条件的图片地址，返回到一个列表<img
#爬取图片超链接中的url
#<img src=图片地址/>
#src="(.*?)\.jpg"   出去后缀
#'src="(.*?)"'
#此网页格式：<img data-original="http://www.jitaotu.com/wp-content/uploads/2020/01/4-2.jpg"/>

list_photo = re.findall(r'<img data-original="(.*?)"',data,re.I|re.S|re.M) #r防止转义
title = re.findall(r'<title>(.*?)</title>',data) #r防止转义
#post_name = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))#以时间戳为文件夹目录名
path = 'C://Users/lx223/Desktop/图虫/'+str(title[0])  #按照当前时间创建新的文件夹

os.mkdir(path)
print('成功创建文件夹'+path+'并保存')
n=1
for i in list_photo:
    try:
        request.urlretrieve(i,path+'/%s.jpg' %n)  #将网络资源下载到本地，本地路径
    except Exception as e:
        print(e)
    finally:
        print('图片%s下载成功'%n)
    n=n+1
print('download successful!')
