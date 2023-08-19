import pandas as pd
df=pd.read_excel('C:/Users/Administrator/Desktop/Copy of 2023年5月数据-CT.xls','PWC5月开票') #The address of the file to be read and the sheet
print(df.columns) #Check the index of columns

split_list=df['Billing号码'].str.split(',') #Split "Billing号码" column
flat_list = split_list.explode().astype(int, errors='ignore') #Spreading split multiple columns into a single row
flat_list = flat_list.reset_index(drop=True) #Reduce the above rows to one column
print(flat_list)

writer = pd.ExcelWriter('C:/Users/Administrator/Desktop/output.xls') #The address of the file to be written
flat_list.to_excel(writer, sheet_name='Sheet1') #Write flat_list in the appointed file
writer.save()







