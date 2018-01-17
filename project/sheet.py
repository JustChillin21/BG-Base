# ndb='09:00'
# meal_1=('14:30','15:00')

# meal_1=None
# meal_2=None
start=None
crewcall=None
wrap=None
days_of_week=None
time=None
ndb=time

clock={
    'start':None,
    'end':None
}

lunch_1=clock
lunch_2=clock

meals={
    'ndb':ndb,
    'meal_1':lunch_1,
    'meal_2':lunch_2
}

hours={
    'start':start,
    'crew':crewcall,
    'wrap':wrap,
    'travel':clock
}

Call_Sheet={
    'date':days_of_week,
    'hours':hours,
    'meals':meals
}

sheet=[]
sheet.append(Call_Sheet)
# sheet[0]['meal_1']=clock
# sheet[0]['meal_2']=clock
print(sheet[0]['meals']['meal_1'])
print(sheet[0])
print(sheet[0]['hours']['travel']['start'])