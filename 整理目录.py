#因为最近整理电子书，文件夹套文件夹，书籍查找起来繁琐，
# 所以想试着写一个Python代码能够将文件夹的文件名写入一个txt中，方便以后查找
#2020.02.28

import os
def create_dir(filepath_dir):               #参数filepath-dir表示当前文件夹名，当遇到子文件夹时改变
        for line in os.listdir(filepath_dir):      #获取目录中的文件及子目录列表
            if os.path.isfile(os.path.join(filepath_dir,line)):           #是文件则写入到dir.txt
               f.write(line+'\n')
              
            elif os.path.isdir(os.path.join(filepath_dir,line)):          #若为文件夹则递归调用create_dir()函数进行输出
                f.write('-----'+line+'-----\n')        #标识子目录名字,只能2级
                create_dir(os.path.join(filepath_dir,line))
              

filepath = input('请输入一个路径： ')    #输入获取文件夹目录,格式如：c:\\Users\lx223\Desktop\   
f = open(os.path.join(filepath,'dir.txt'),'w+')                  #在当前目录新建一个dir.txt文件   
if filepath == '':
        print("请输入正确的路径！")
else:
     create_dir(filepath)


#1.0能够实现写出当前目录下所有文件及其子文件夹中所有文件名，写在dir.txt中
#缺陷：1.所有文件夹表示相同，不能分辨出哪个是子文件夹，层次性不强
