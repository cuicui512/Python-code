import re
'''
#match与serch
print(re.match('book','books')) 
print(re.search('book','sbooks'))
'''
'''
#findall
python = 'python2 python3 are all python'
print(re.findall('python',python))
'''


'''
#split
python = 'python2 python3 are all python'
print(re.split(' ',python))
'''

'''
#sub
python = 'python2 python3 are all python'
print(re.sub('python','java',python))
'''

#正则表达式爬取title标签间的内容
#<title>标题名</title>
#'<title>(.*?)</title>'
'''
import re
from urllib import request
url = request.urlopen('http://www.jitaotu.com/xinggan/79973-all.html')
data = url.read().decode('utf-8')
title = re.findall(r'<title>(.*?)</title>',data) #r防止转义
print(title[0])
'''

#正则表达式爬取超链接标签的url
#<a href=url>超链接标题</a>
#(? <=href=\".+?(?=\')")|(? <=href=\).+?(? =\')
#url1 = re.findall(r'(? <=href=\".+?(? =\)")|(? <=href=\').+?(? =\')',data,re.I|re.S|re.M)

#爬取图片超链接中的url
#<img src=图片地址/>
#src="(.*?)\.jpg"   出去后缀
#'src="(.*?)"'
#此网页格式：<img data-original="http://www.jitaotu.com/wp-content/uploads/2020/01/4-2.jpg"/>
import re
from urllib import request
urls = request.urlopen('http://www.jitaotu.com/xinggan/79973-all.html')
data = urls.read().decode('utf-8')
list_photo = re.findall(r'<img data-original="(.*?)"',data,re.I|re.S|re.M)
print(list_photo)