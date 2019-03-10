#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:04:31 2018

@author: loganbe
"""
#%%
import datetime
import pickle

#%% Find Data and Time Info
dateinfo = datetime.datetime.today() #Find Todays Date and Time

#Disect the Information
year = dateinfo.year
month = dateinfo.month
day = dateinfo.day
weekday = dateinfo.weekday()
hour = dateinfo.hour
minute = dateinfo.minute

months = ['January','February.','March','April','May','June','July',
          'Augest','Septemp','October','November','December'] #Bank Of Months

weekday_convert = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] #Bank of Days of Week

#Convert 24hr clock to 12hr clock
if hour > 12: 
    hour = hour-12
    suffixTime = 'pm'
else:
    suffixTime = 'am'
#Convert Number day of week to String
DayOfWeek = 'Sunday';#weekday_convert[weekday]

#Convert Month Number to Month Word
monthword = months[month-1]
if day == 1 or day == 21 or day == 31:
    suffix = 'st'
elif day == 2 or day == 22:
    suffix = 'nd'
elif day == 3 or day == 23:
    suffix = 'rd'
else:
    suffix = 'th'    

print(DayOfWeek + ', ' + monthword + ' ' + str(day)+suffix)
print(str(hour)+':'+str(minute),suffixTime)

#%% Import Old Data Info Save New Date Information
Import_Info = open("Date.pickle","rb") #Import Old Date
OldInfo = pickle.load(Import_Info)

Upload_Info = {'Day':day,'WeekDay':DayOfWeek,'Month':monthword,'Year':year,'Hour':hour,'Min':minute} #Save New Date
pickle_out = open("Date.pickle","wb")
pickle.dump(Upload_Info,pickle_out)
pickle_out.close()

#%% Import Old Info 
Import_Info = open("Money.pickle","rb") #Import Old Money
OldMoney = pickle.load(Import_Info)

Import_Info = open("Left_Over.pickle","rb") #Import Old LeftOvers
OldLeftOver = pickle.load(Import_Info)
LeftOvers = OldLeftOver['LeftOvers']

Import_Info = open("Settings.pickle","rb") #Import Old Settings
Settings = pickle.load(Import_Info)
Allowance = int(Settings['Allowance']);

#%% Check if New Day/Week/Month/Year
if OldInfo['Day'] != day:
    Daily = [0]; #If New Day; Reset
else:
    Daily = OldMoney['Daily'] #Else Use Old Day Value

if OldInfo['WeekDay'] != 'Sunday' and DayOfWeek == 'Sunday': #Last input was Not Sunday but today Is Sunday
    if OldMoney['Weekly'] > [0]: #If New Week and Money was Left Over
        LeftOverNew = OldMoney['Weekly'] #Update LeftOvers
        LeftOvers = LeftOvers + LeftOverNew[0]   
    Weekly = [Allowance]; #Reset Week
else:
    Weekly = OldMoney['Weekly'] #Else Use Old Week Value

if OldInfo['Month'] != monthword:
    Monthly = [0]; #If New Month; Reset
else:
    Monthly = OldMoney['Monthly'] #Else Use Old Month Value

if OldInfo['Year'] != year:
    Yearly = [0]; #If New Year; Reset
else:
    Yearly = OldMoney['Yearly'] #Else Use Old Year Value
    
#%% Save In Case No Changes Made
Daily_Past = OldMoney['Daily']; Weekly_Past = OldMoney['Weekly'] 
Monthly_Past = OldMoney['Monthly']; Yearly_Past = OldMoney['Yearly']

Money_Info = {'Daily':[sum(Daily_Past)],'Weekly':[sum(Weekly_Past)],'Monthly':[sum(Monthly_Past)],
              'Yearly':[sum(Yearly_Past)]}
pickle_out = open("Money.pickle","wb")
pickle.dump(Money_Info,pickle_out)
pickle_out.close() 

Left_Over = {'LeftOvers':LeftOvers}
pickle_out = open("Left_Over.pickle","wb")
pickle.dump(Left_Over,pickle_out)
pickle_out.close()
#%% Main Body
exitflag = 1 #Use to Check if Exitied Code
if DayOfWeek == 'Sunday' and hour == 2 and minute == 30:
        print('Exiting')
else:
    while exitflag == 1:
        Which = input('Input, LeftOver, View, Settings or Exit? ') #Main Options
        if Which == 'Input' or Which == 'input': #If Chosen Input
            try:
                Money = float(input('How Much Money? ')) 
                
                if Money > 0: #If Spending Money
                    print('Spent $', Money)
                else: #If Refunding
                    print('Refund $', Money)
                
                #Increase Daily/Monthly/Yearly
                Daily.append(Money) 
                Monthly.append(Money)
                Yearly.append(Money)
                
                if (sum(Weekly)-Money) < 0: #If you spent over your allowance
                    print()
                    print('WARNING')
                    print('YOU HAVE GONE BELOW YOUR ALLOWANCE')
                    print()
        
                    if LeftOvers > 0: #If You have some leftovers and want to dip into it
                        print()
                        print('You Have $',LeftOvers,'In LeftOvers')
                        RollOver = input('Would You Like To Use Money From LeftOver? ')
                        if RollOver == 'yes' or RollOver == 'Yes': #If you want to Take From LeftOvers
                            LeftOvers = LeftOvers - Money #Take from LeftOvers
                            if LeftOvers < 0: 
                                Weekly.append(LeftOvers) 
                                LeftOvers = 0
                        else:
                            Weekly.append(-Money)
                    else:
                        Weekly.append(-Money)
                else:
                    Weekly.append(-Money)
        
                Money_Info = {'Daily':[sum(Daily)],'Weekly':[sum(Weekly)],'Monthly':[sum(Monthly)],'Yearly':[sum(Yearly)]}
                pickle_out = open("Money.pickle","wb")
                pickle.dump(Money_Info,pickle_out)
                pickle_out.close()
                
                Left_Over = {'LeftOvers':LeftOvers}
                pickle_out = open("Left_Over.pickle","wb")
                pickle.dump(Left_Over,pickle_out)
                pickle_out.close()
                
            except KeyboardInterrupt:
                print('Interupted')
            
        if Which == 'LeftOver' or Which == 'leftover' or Which == 'Leftover' or Which == 'leftOver':
            try:
                print("Leftover Available:",LeftOvers)
                Money = float(input('How Much Money? '))
                
                if LeftOvers >= Money:
                    LeftOvers = LeftOvers - Money
                    Left_Over = {'LeftOver':LeftOvers}
                    pickle_out = open("Left_Over.pickle","wb")
                    pickle.dump(Left_Over,pickle_out)
                    pickle_out.close()
                else:
                    print('Not Enough LeftOvers')
            
            except KeyboardInterrupt:
                print('Interupted')
            
        if Which == 'Settings' or Which == 'settings' or Which == 'Setting' or Which == 'setting':
            try:
                print('What Would You Like To Change? ')
                print('Allowance:', Allowance)
                print('Reset LeftOvers:',LeftOvers)
                print('Cancel')
                Sett = input()
                
                if Sett == 'Allowance' or Sett == 'allowance':
                    NewAllow = input('New Allowance: ')
                    Sett_Info = {'Allowance':NewAllow}
                    pickle_out = open("Settings.pickle","wb")
                    pickle.dump(Sett_Info,pickle_out)
                    pickle_out.close()
                    
                if Sett == 'Reset LeftOvers' or 'reset leftovers' or 'Reset leftovers' or 'reset Leftovers':
                    LeftOvers = 0
                    Left_Over = {'LeftOvers':LeftOvers}
                    pickle_out = open("Left_Over.pickle","wb")
                    pickle.dump(Left_Over,pickle_out)
                    pickle_out.close()
                    
                else: 
                    print('Exiting')
                    
            except KeyboardInterrupt:
                print('Interupted')
        
        if Which == 'View' or Which == 'view':
            print('Current Weekly Allowance Left:', sum(Weekly))
            print('LeftOvers:',LeftOvers)
            print('Money Spent today: ', sum(Daily))
            print('Money Spent this Month: ', sum(Monthly))
            print('Money Spent this Year: ', sum(Yearly))
    
        if Which == "Exit" or Which == "exit":
            print('Exiting')
            exitflag = 0;