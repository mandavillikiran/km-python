import pandas as pd
import numpy as py
df1 = pd.read_csv('C:\\Users\\kiran\\Downloads\\training-attendanceT (1)\\SECTION1.csv',names = ["Sno", "Department", "Branch", "Semester", "Course", 
      "RegistrationNo", "StudentName", "Date", "Slot group", "Time", "ClassConducted", "ClassAttended"])
df = df1[['RegistrationNo','StudentName','Date','ClassAttended']]

#sa = df.pivot(index = "Date", columns="RegistrationNo",values="ClassAttended").reset_index()
#df.groupby(['Date', 'RegistrationNo', 'StudentName', 'ClassAttended']).Date.max().unstack('ClassAttended')
#print(df)
#df.pivot(index = "RegistrationNo", columns="Date",values="ClassAttended")
#print(df)
df[['RegistrationNo','StudentName']].drop_duplicates(keep='first')
#print(df)
sa = df.pivot_table(index = "Date", columns="RegistrationNo",values="ClassAttended")
print(sa)
#sa.to_csv("C:\\Users\\kiran\\Downloads\\sa.csv") 