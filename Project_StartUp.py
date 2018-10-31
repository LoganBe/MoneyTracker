#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:39:54 2018

@author: loganbe
"""
import datetime
import pickle

#%%
dateinfo = datetime.datetime.today()

year = dateinfo.year
month = dateinfo.month
day = dateinfo.day
weekday = dateinfo.weekday()
hour = dateinfo.hour
minute = dateinfo.minute

months = ['January','February.','March','April','May','June','July',
          'Augest','Septemp','October','November','December']

weekday_convert = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


if hour > 12: 
    hour = hour-12
    suffixTime = 'pm'
else:
    suffixTime = 'am'

DayOfWeek = weekday_convert[weekday]

monthword = months[month-1]
if day == 1 or day == 21 or day == 31:
    suffix = 'st'
elif day == 2 or day == 22:
    suffix = 'nd'
elif day == 3 or day == 23:
    suffix = 'rd'
else:
    suffix = 'th'    

Upload_Info = {'Day':day,'WeekDay':DayOfWeek,'Month':monthword,'Year':year,'Hour':hour,'Min':minute}
pickle_out = open("Date.pickle","wb")
pickle.dump(Upload_Info,pickle_out)
pickle_out.close()
#%%
flag = 1;
while flag == 1:
    Allowance = input('What Would You Like To Set As Your Allowance? ')
    try:
        Allowance = float(Allowance)
        flag = 0
    except ValueError:
        print('Please Use and Integer or a Float')
#%%

Money_Info = {'Daily':[0],'Weekly':[Allowance],'Monthly':[0],'Yearly':[0]}
pickle_out = open("Money.pickle","wb")
pickle.dump(Money_Info,pickle_out)
pickle_out.close()

Left_Over = {'LeftOvers':0}
pickle_out = open("Left_Over.pickle","wb")
pickle.dump(Left_Over,pickle_out)
pickle_out.close()

NewAllow = input('New Allowance: ')
Sett_Info = {'Allowance':Allowance}
pickle_out = open("Settings.pickle","wb")
pickle.dump(Sett_Info,pickle_out)
pickle_out.close()