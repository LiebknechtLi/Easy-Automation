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
    has_22 = False
    has_23 = False

    for num in row: #遍历row中的数字
        if num[2:4] == '22':
            has_22 = True
        elif num[2:4] == '23':
            has_23 = True   #传参+修改参数

    if has_23 and not has_22:
        res.append('今年前期')
    elif has_23 and has_22:
        res.append('23合并')
    else:
        res.append('22及以前') #18-33行的功能，是判断Row Labels行中包含的每个数字的2-4位是否含22、23。同时含有，返回“23合并‘；只含有23，返回”今年前期“；其他情况，返回”22及以前“

res = np.array(res)
df['开票时间'] = res
print(df['开票时间'])

df.iloc[1:, 4] = df.iloc[1:,4].astype(float)
df.iloc[1:, 5] = df.iloc[1:,5].astype(float) #一直运行到这里都没有问题。。。

condition1=df.iloc[1:, 4]-df.iloc[1:, 5]>0
condition1 = condition1.astype(int) #”condition1等是布尔型Series,其值只能是True/False,不能直接使用[np.newaxis]扩展维度。我们需要把布尔值转换为整数型,才可以扩展维度。“
condition1 = condition1[np.newaxis]

condition2=df.iloc[1:, 4]-df.iloc[1:, 5]==0
condition2 = condition2.astype(int)
condition2 = condition2[np.newaxis]

condition3=df.iloc[1:, 4]-df.iloc[1:, 5]<0
condition3 = condition3.astype(int)
condition3 = condition3[np.newaxis]  #代码报错发生在39-52行。数组维度出错，错误的原因我一直没有理解

conditions = [condition1, condition2, condition3]
choices = np.array(['提前开票', '开完', '部分开票'])

x1=choices[0]
x2=choices[1]
x3=choices[2]

df['开票状态'] =np.where(condition1,x1,
                       np.where(condition2,x2,
                               np.where(condition3,x3,'null'))) #根据conditions返回choices


print(df)
writer = pd.ExcelWriter('C:/Users/Administrator/Desktop/output.xls') #写入文件的地址
df.to_excel(writer, sheet_name='Sheet1') #写入上一行的指定文件
writer.save()