import os

#网上的
#输出当前目录下的文件/文件夹路径包含名称
'''
def print_dir():
    filepath = input('请输入一个路径： ')
    if filepath == '':
        print("请输入正确的路径！")
    else:
        for i in os.listdir(filepath):      #获取目录中的文件及子目录列表
            print(os.path.join(filepath,i)) #把路径组合起来

print_dir()
'''

#自己写的
#输出当前目录下的文件/文件夹名称
for line in os.listdir('.'):   #得到存储文件信息的列表 ,并循环输出列表中的信息
    print(line)

# 列出当前目录下的所有子目录
for line in os.listdir('.'):
    if os.path.isdir(line):
        print(line)

# 列出当前目录下的所有文件
for line in os.listdir('.'):
    if os.path.isfile(line):
        print(line)

        
# 列出当前目录下所有py文件
for line in os.listdir('.'):
    if os.path.isfile(line) and os.path.splitext(line)[1] == '.py':
        print(line)