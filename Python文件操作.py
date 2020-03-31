#打开文件
f = open('C://Users/lx223/Desktop/test.txt','w+')
#关闭文件
#f.close()
#写入文件
f.write('Hello world!'+'\n')
f.write('Hello world!')
#读取文件,可以设置读取字节数，若不设置则默认读取所有，每一次调用read函数会移动光标位置，下一次读取时从当前光标处开始
#print(f.read(2))
#print(f.read())
#按行写入
#f.writelines(['hello\n','the\n','world\n'])
#按行读取
#print(f.readline())     #返回一行内容
#print(f.readlines())    #返回所有行信息的列表



#CSV库操作
#使用CSV模块读取
'''
import csv
with open('C://Users/lx223/Desktop/text.csv','r')as f:
    #w = csv.writer(f)
   # w.writerow(['1','2','3'])
    #w.writerow(['first','second','third'])
    data = csv.reader(f)
    for line in data:
        print(line)
'''