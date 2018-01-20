from datetime import timedelta
from sheet_class import TimeSheet, Lunch, Travel, Hours, Meals
# from time_calculations import mod_date
import time_calculations

print('Date')
work_date=('2017-12-31')
# work_date=input("Please enter the date: ")
Date=time_calculations.mod_date(work_date)
TimeSheet.date=Date
print('Lunch 1...')
lunch_1=Lunch(start='13:45', end='14:15')
print('Lunch 2...')
lunch_2=Lunch()
print('Travel Time...')
travel=Travel(to_set=':20', from_set=':20')
print('Hours...')
hours=Hours(start='09:00', crew='09:00', wrap='24:21', travel=travel)
# hours_start=hours.start - travel_time.to_set
hours_start=hours.start - timedelta(hours=0,minutes=20)
ndb=True
print('Meals...')
meals=Meals(ndb=ndb, lunch_1=lunch_1, lunch_2=lunch_2)

print('\n Report\n')

temp=TimeSheet(Date,hours,meals)

sheets=[]
sheets.append(temp)
print(sheets[0])
work_time=sheets[0].hours.total_hours-sheets[0].meal_1.total_time

print(work_time)
print(time_calculations.converttime(work_time))
