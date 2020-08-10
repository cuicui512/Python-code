# 批量更改 .jpg  to  .png
import os


def find_dir(filepath_dir):               #参数find-dir表示当前文件夹名，当遇到子文件夹时改变
        for line in os.listdir(filepath_dir):      #获取目录中的文件及子目录列表,line是存储的元组,  eval()防止地址被转义
            if os.path.isfile(os.path.join(filepath_dir,line)):           #是文件则输出文件名
                # print(line)
                if_jpg(line)
                
            elif os.path.isdir(os.path.join(filepath_dir,line)):          #若为文件夹则递归调用find_dir()函数进行输出
                # print("--子目录--")        #标识子目录名字
                find_dir(os.path.join(filepath_dir,line))
          

def if_jpg(file_name):  #判断格式为.jpg
    if os.path.splitext(file_name)[1] == '.jpg':      # os.path.splitext(“文件路径”)    分离文件名与扩展名
        # print(file_name[0])
        file_old_name = file_path + os.sep + file_name      # os.rename()的参数是需要完整路径的
        #print(file_old_name)
        file_new_name = file_path + os.sep + os.path.splitext(file_name)[0] +".png"    # 人为的生成新的名字，字符串
        #print (file_new_name)
        rename(file_old_name,file_new_name)     # 调用改名函数rename()，注意os.rename()的参数是需要完整路径的
        

def rename(old_name,new_name):  # 重命名文件
    os.rename(old_name,new_name)     # os.rename(原文件名，新文件名） : 对文件或目录改名
    

if __name__=="__main__":
    
    #文件路径写死了可以参考： file_path = r"C:\Users\lx223\Desktop\QQ"
    file_path = input('请输入一个路径： ')    #输入获取文件夹目录,格式如：C:\Users\lx223\Desktop\QQ
    find_dir(file_path) 
    print("Done!")  
    
   
    
  

