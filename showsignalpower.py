import xlrd,xlwt,xlutils.copy
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

str ='C7   C5   C5   C4   C5   C6   C7   C6   C6   C1   C1   C1   B5   B8   B3   BB   D0   D2   D0   D1   B8   B7   B9   BB   B9   D0   D0   C0   C9   C7   C6   C6   C6   C4   C4   C7   C4   C3   C2   C5   C5   C1   C3   C5   C5   B5   B5   B5   B5   B6   C5   C4   C8   C8   B5   B5   B0   CA   CA   D0   CC   CD   CE   B1   B2   C4   CD   CE   CB   CD   CB   CF   C9   C3   CA   CB   CB   BB   B8   BA   BD   B6   B9   B8   BB   B7   B5   BA   B7   B6   B5   B8   B5   B5   B5   B9   B9   B8   BA   B7   BA   BA   BA   B7   B7   B7   B8   CD   CA   C9   C9   C9   C9   C9   C9   C9   C9   D0   D1   D0   D0   D0   D1   D2   D1   D1   D2   D1   D0   D1   D1   D0   D0   D0   D1   D1   D0   D1   D1   D0   D1   D0   D1   D0   D1   D0   D0   C5   C5   C4   B8   B7   B8   C9   C9   C9   C9   CA   C9   C9   C9   C9   C9   C9   C9   C9   C9   C9   C9   D1   D0   BB   C0   C0   BD   BA   BE   BA   BE   BD   BC   C0   B8   B8   C1   C1   B7   B2   C9   C9   C9   C9   C9   CA   C9   B5   B5   B3   B4   B5   B5   B5   B3   B3   B7   B6   B5   B4   B6   B8   B8   B8   B8   B8   B7   B6   CC   CC   D1   D1   D0   D0   D1   D1   D1   B4   B5   B4   D0   D1   D0   D0   D0   D0   D0   D1   D0   D2   B3   B4   B3   C9   CA   C9   CA   C9   C9   C9   CA   C9   CA   CA   CA   CA   CA   C9   C9   C9   C9   C9   CA   C9   C9   C9   CA   C9   CA   B4   B2   B0   B2   B1   B4   B2   B1   D0   D1   D0   D0   D0   C9   C9   C9   C9   C9   C9   D1   D0   D0   D0   C3   C2   C3   C4   C3   C3   BA   C6   CB   C5   C0   BF   C0   BF   BE   BF  '
arr=str.split('   ')
for i in range(len(arr)):
    ws.write(i, 0, int(arr[i], 16))

wb.save('example.xls')