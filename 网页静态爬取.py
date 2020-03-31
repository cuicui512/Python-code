'''
#urllib库,其中有5个模块
import urllib
help(urllib)
'''


#request模块
#urlopen()函数   自带的方法与文件操作使用一样

#打印百度首页源代码的内容:
import urllib.request 
html = urllib.request.urlopen('https://www.baidu.com')
print(html.read())


'''
#urlretrieve()函数
import urllib.request 
url = 'https://www.baidu.com/img/bd_logol.png'
urllib.request.urlretrieve(url,'C:/Users/lx223/Desktop/logol1.png')
'''
