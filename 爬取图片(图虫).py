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
#f = open('C://Users/lx223/Desktop/哔哩哔哩.html','w+')  #把网页源码爬下来分析正则表达式
#f.write(data)  
#找到的图片格式：
# <img id="image543672546" class="multi-photo-image" src="https://photo.tuchong.com/1307602/f/543672546.jpg" alt="">

#找到所有符合条件的图片地址，返回到一个列表
list_photo=re.findall('https://photo.tuchong.com.+.jpg',data)#正则表达式基本用法 格式：开头字符串.+.结尾字符串

print(list_photo)#输出图片在网页审查元素中的表达式，方便查错
post_name = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))#以时间戳为文件夹目录名

path = 'C://Users/lx223/Desktop/图虫/'+str(post_name)  #按照当前时间创建新的文件夹
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
