import pandas as pd

#reading excel sheet 
ff=pd.read_excel('t2.xlsx',sheet_name='Sheet')
#extracting date components from datetime.datetime format date
ff['year']=pd.DatetimeIndex(ff['Date']).year
ff['month']=pd.DatetimeIndex(ff['Date']).month
ff['day']=pd.DatetimeIndex(ff['Date']).day

ff['weekday'] = ff['Date'].dt.dayofweek

#creating new file
writer= pd.ExcelWriter('output.xlsx')
#writing from data frame to file
ff.to_excel(writer)
writer.save()