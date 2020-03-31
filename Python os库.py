import os
#返回操作系统类别，posix , nt , java， 对应linux/windows/java虚拟机
#print(os.name)    
#返回电脑中环境变量的目录
#print(os.environ)   
# 查看当前目录的绝对路径
#print(os.path.abspath('.'))

#注意，将两个路径合成一个时，不要直接拼接字符串，而是要通过
# os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
#print(os.path.join(os.path.abspath('.'), 'testdir'))

#创建目录
#os.mkdir()
#删除目录
#os.rmdir()
#重命名
#os.rename()

#分割路径
#print(os.path.split("c:\\Users\lx223\Desktop\python\Python os库.py"))

#分割可以直接得到文件扩展名
#print(os.path.splitext("c:\\Users\lx223\Desktop\python\Python os库.py"))

#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
'''
print(os.listdir('.'))       #os.listdir()返回的是列表类型
for line in os.listdir('.'):   #得到存储文件信息的列表 ,并循环输出列表中的信息
    print(line)
'''
#os.path.isdir()判断是否为目录

# 列出当前目录下的所有子目录
'''
for line in os.listdir('.'):
    if os.path.isdir(line):
        print(line)
'''


# 列出当前目录下的所有文件
'''
for line in os.listdir('.'):
    if os.path.isfile(line):
        print(line)
'''


# 列出当前目录下所有py文件
for line in os.listdir('.'):
    if os.path.isfile(line) and os.path.splitext(line)[1] == '.py':
        print(line)
