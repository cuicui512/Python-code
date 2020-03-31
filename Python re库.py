import re #正则表达式操作库

#match与serch  匹配 
#  mach()从字符串起始位置开始匹配，匹配成功返回匹配对象，失败则返回None
#  search()不要求从起始位置开始匹配
print(re.match('book','books')) 
print(re.search('book','sbooks'))


#findall 在爬虫中使用最频繁，用于查找字符串中所有符合正则表达式的字符串，返回一个列表
python = 'python2 python3 are all python'
print(re.findall('python',python))




#split   按某个字符将字符串分解为若干子字符串
python = 'python2 python3 are all python'
print(re.split(' ',python))



#sub    将字符串中某些字符替换为特定字符串
python = 'python2 python3 are all python'
print(re.sub('python','java',python))




