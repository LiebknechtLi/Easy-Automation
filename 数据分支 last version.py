import pandas as pd

df=pd.read_excel('C:/Users/Administrator/Desktop/Copy of 2023年5月数据-CT.xls','Sheet5') #读取的文件地址及表单号
print(df.columns) #检查列索引
print()

import numpy as np

data = np.array(df['Row Labels.1'])

res=[]
for row in data:
    if isinstance(row, float): #遍历表格中的Row Labels行，若为浮点数，形成列表
        row = [row]
    elif isinstance(row, str): #遍历表格中的Row Labels行，若为字符串，形成列表
        row = [row]

    row = str(row)
    row = row.strip("[]")
    row = row.replace("'", "")
    row_values = row.split(",")  #去除引号和方括号，使用逗号拆分字符串并形成列表

    row_integers = []
    for value in row_values:
        if value != 'nan':
          value = int(value)
          row_integers.append(value) #将字符串转为整数

    has_22 = False
    has_23 = False

    for num_int in row_integers: #遍历row中的数字
        if 1123000000 > num_int > 1122000000:
            has_22 = True
        elif num_int > 1123000000:
            has_23 = True   #传参+修改参数

    if has_23 and not has_22:
        res.append('今年前期')
    elif has_23 and has_22:
        res.append('23合并')
    else:
        res.append('22及以前') #判断数字大小，在新列中返回不同的值

res = np.array(res)
df['开票时间'] = res
print(df['开票时间'])

df.iloc[1:, 4] = df.iloc[1:,4].astype(float)
df.iloc[1:, 5] = df.iloc[1:,5].astype(float)

condition1=df.iloc[1:, 4]-df.iloc[1:, 5]>0
condition1 = condition1.astype(int)
condition1 = pd.Series([0] + [i for i in condition1])

condition2=df.iloc[1:, 4]-df.iloc[1:, 5]==0
condition2 = condition2.astype(int)
condition2 = pd.Series([0] + [i for i in condition2])

condition3=df.iloc[1:, 4]-df.iloc[1:, 5]<0
condition3 = condition3.astype(int)
condition3 = pd.Series([0] + [i for i in condition3]) #设立条件+填充表头标题的维度

conditions = [condition1, condition2, condition3]
choices = np.array(['提前开票', '开完', '部分开票'])

x1=choices[0]
x2=choices[1]
x3=choices[2]

df['开票状态'] =np.where(condition1,x1,
                       np.where(condition2,x2,
                               np.where(condition3,x3,'null'))) #根据conditions返回choices
print(df)

df.to_excel('C:/Users/Administrator/Desktop/output.xlsx', index=False)