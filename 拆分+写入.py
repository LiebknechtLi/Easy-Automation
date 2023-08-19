import pandas as pd
df=pd.read_excel('C:/Users/Administrator/Desktop/Copy of 2023年5月数据-CT.xls','PWC5月开票') #读取的文件地址及表单号
print(df.columns) #检查列名
split_list=df['Billing号码'].str.split(',') #拆分”Billing号码“列
flat_list = split_list.explode().astype(int, errors='ignore') #将拆分出的多列摊开为一行
flat_list = flat_list.reset_index(drop=True) #将上述行还原为一列
print(flat_list)
writer = pd.ExcelWriter('C:/Users/Administrator/Desktop/output.xls') #写入文件的地址
flat_list.to_excel(writer, sheet_name='Sheet1') #写入上一行的指定文件
writer.save()







