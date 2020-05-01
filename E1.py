import pandas as pd
import numpy as py
student_data = pd.read_csv('//data//training//SECTION1.csv',names = ["Sno", "Department", "Branch", "Semester", "Course", 
      "RegistrationNo", "StudentName", "Date", "Slot group", "Time", "ClassConducted", "ClassAttended"])
unique_reg_and_name_combo = student_data[['RegistrationNo','StudentName']].drop_duplicates(keep='first')
# Unique_date value
datecolumns = list(student_data['Date'].unique())
datecolumns
# FINAL DATASET COLUMNS
final_columns = list(unique_reg_and_name_combo.columns) + datecolumns
empty_dataframe = pd.DataFrame(columns=final_columns)
empty_dataframe['RegistrationNo'] = unique_reg_and_name_combo['RegistrationNo']
empty_dataframe['StudentName'] = unique_reg_and_name_combo['StudentName']
empty_dataframe.reset_index(inplace=True)
empty_dataframe.drop('index',axis=1,inplace = True)
rownum = 0
for eachregnumber in empty_dataframe['RegistrationNo']:
    colnum = 2
    for eachdate in datecolumns:
        empty_dataframe.iat[rownum,colnum] = student_data[(student_data['RegistrationNo'] ==eachregnumber)&
                                                       (student_data['Date'] == eachdate)]['ClassAttended'].sum()
        colnum = colnum+1
    rownum = rownum+1

with open('//data//training//testcase.txt') as f:
     content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
tc = content[0]
#print(tc)
lc = len(content)
c = 1 
i = 1
while c in range(lc):    
    reg_num = content[c]
    c = c + 1
    reg_date = content[c]
    nod = empty_dataframe.loc[empty_dataframe['RegistrationNo']==reg_num,reg_date].values[0]
    path = "//code// + "output" + str(i) + ".txt"
      #print(path)
    ff= open(path,"w") 
    ff.write(str(nod))
    ff.close()
    i = i + 1
    c = c + 1                                            
f.close()    