
import xlrd
import xlwt
from xlutils.copy import copy
time=1
path=input('请输入标准的工作簿路径：')
xlsl=xlrd.open_workbook(path)
number=input('要处理的是第几个工作表（首个工作表是第0个）：')
number=int(number)
table=xlsl.sheet_by_index(number)
new_excel=copy(xlsl)
new_sheet=new_excel.get_sheet(number)
pattern=xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=5
borders=xlwt.Borders()
borders.top=xlwt.Borders.THIN
borders.bottom=xlwt.Borders.THIN
borders.left=xlwt.Borders.THIN
borders.right=xlwt.Borders.THIN
style=xlwt.XFStyle()
style.pattern=pattern
style.borders=borders
cloum=input('请输入待处理的列数，首列为第0列：')
cloum=int(cloum)
value=input('请输入门限制：')
value=float(value)
nrows=table.nrows
for i in range(1,nrows):
    a=table.row_values(i)[cloum-1:cloum].pop(0)
    if type(a)!=float:
        print('你输入的列不是数字列，可能输入有误，请检测')
        print('当前输入的列是'+'"'+a+'"'+'列'+',请校正')
        break
    else:
        a=float(a)
        if a>value:
            new_sheet.write(i,cloum-1,a,style)
            new_excel.save(r'D:/new_excel.xls')
            time=time-1
            if time<0:
                continue
            else:
               print('生成的新文件保存在目录D:/new_excel.xls下')