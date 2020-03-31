import re

'''
a = 1   #字符串的基本操作
b= 1.0
c= 2j
print(type(a),type(b),type(c))
d = "string"
e = 'string'    #单引号和双引号通用
print(d[1])     #取得数组元素
print(d[2:4])   
print(d[::-1])  #翻转字符串
print(d+e)      #连接字符串

a = '%sa' % 1   #%的使用，用于指定参数将以何种形式拼接入字符串
print(a)
print('%sa%rb%fc' % (1,1,1))    #%s（直接获取字符串内容）和%r（使用变量原始数据）都是字符串格式，
a = '%s' % 'one'
b = '%r' % 'one'
print(a)
print(b)

#{}.format()完成字符串的拼接
print('{0}{1}'.format('a',2))   #0,1指定参数位置
print('{a}{b}'.format(a='c',b='d')) #通过参数名调用

'''

'''
#List的基本操作
a = ['a','b','v','d']
print(a)
print(a[1],a[2])    #取元素
print(a[1:3])       #切片操作
print(a[:-1])       #不取到最后一位
print(a[::-1])      #倒序
del a[1]            #删除第二位
print(a)
a = ['a','b','v','d']
b = set(a)          #去重，利用set()集合去重，再利用list()重新转换为列表
print(list(b))

a = ['a','b','v','d']     
print(a+a)          #拼接
a.append([1,2,3])    #利用append()拼接，append(list)将列表作为一个元素加入到列表中
print(a)
a.extend(a)      #利用extend()拼接，等同于+号
print(a)
a.insert(2,10)   #插入
print(a)
print(a.insert(2,10))       #这些函数不能直接写在print里面，不然会是none,但是会被执行
print(a) 

a = ['a','b','v','d']       #查找，返回元素第一次出现的位置,查不到就error
print(a.index('v'))

#列表属性操作
a = [1,2,3,4,5,6]
print(len(a))   #返回列表长度
print(max(a))   #返回列表最大值
print(min(a))   #返回列表最小值
print(sum(a))   #返回列表求和
print(a.pop(1))   #利用pop()移除列表中的一个元素，参数表示元素位置
print(a.count(1))   #统计参数的个数
a.remove(1)         #删除某个参数
print(a)
a.reverse()         #反向返回
print(a)         
sorted(a)           #排序，sorted()不会修改列表
print(a)
a.sort()            #排序，a.sort()会修改列表
print(a)
'''


'''
#字典的基本操作
a= {'a':(1,2,3),('b','c'):[4,5,6],'f':'g'}
print(a)
print(a['a'])       #使用key来访问
#print(a[(1,2,3)])   #使用key来访问,不存在则为error

a['a'] = [1,2,3,4]  #对字典元素赋值
print(a)            
a['h'] = 1          #添加字典元素
print(a)
del a['a']          #删除字典元素
print(a)

a= {'a':(1,2,3),('b','c'):[4,5,6],'f':'g'}      
for k in a.keys():          #利用for循环遍历输出keys
    print(k)

for v in a.values():        #利用for循环遍历输出values
    print(v)

for k,v in a.items():       #利用for循环遍历同时输出keys和values
    print(k,v)

a = [1,2,3,4]
b = ['a','b','c','d']
k = dict(zip(b,a))          #利用zip将两个列表合并为字典
print(k)
'''
'''
#元组的基本操作
t = (1,)   #创建一个元素的元组时，末尾加上逗号，不然为简单的赋值语句
t = ('a','b','c','d')       
print(t)        #访问元组
print(t[1])
print(t[1:3] ) #切片
print(t[:-1] ) #切片
'''

'''
#推导式的建立
a = [i*2 for i in range(1,10)]          #构建列表推导式
print(a)

a = (i*2 for i in range(1,10))         #构建生成器generator
print(a)

dic = {'a':2,'b':3,'c':4}               #构建字典推导式
a = {k.upper():v+1 for k,v in dic.items()}
print(a)

b = {i**2 for i in [1,2,3,4,3,2,1]}     #构建集合推导式
print(b)
print(type(b))
'''

'''
#自定义函数
def judge(a,b):
   if a>b:
      return a
   else :
       return b
print(judge(2,4))

#自定义匿名函数
f = lambda a,b :a if a>b else b
print(f(2,4))

'''
'''
#类与对象
class student():
    def __init__(self):
        self.class_name = '1713012'
        self.age = '3'

linxin = student()
print(linxin.class_name,linxin.age)
'''

