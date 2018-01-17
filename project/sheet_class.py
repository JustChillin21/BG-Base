from datetime import datetime, timedelta
import math

class mod_date:
    def __init__(self,date=None):
        if date:
            self.date=datetime.strptime(date, '%Y-%m-%d')
            self.date=self.date.strftime('%Y-%m-%d')
    def __repr__(self):
        return self.date



class check_time:

    @staticmethod
    def roundtime(x, base=6):  # Rounds time up to the nearest 6 minute interval
        if x==0:
            return '00'
        else:
            return int(math.ceil(x / base)) * base



    def __init__(self, time=None, date=None,show=0):
        self.time=time
        self.show=show
        self.date=datetime.strptime(date, '%Y-%m-%d')
        self.new_time=None

        if type(self.time) is datetime:
            # print("We are in Checktime "+datetime.date(time, '%Y-%m-%d %H:%M'))
            return self.time
        else:
            # print("We are in the Else statement of checktime".format(time))
            stime = self.time.split(':')
            wtime = self.time
            ntime = int(stime[0])
            nminute = int(stime[1])
            print('Self Date {}'.format(self.date))
            to_update=self.date
            if ntime > 23:
                ntime -= 24
                add_days = 1

                mntime=str(ntime)
                if len(mntime)<2:stime[0]="0"+mntime

                stime[1] = str(check_time.roundtime(nminute))

                wtime = stime[0]+':'+stime[1]
                if self.show != 0: print(wtime)
                updated_time=datetime.strptime(wtime, '%H:%M')
                to_replace=updated_time.replace(year=to_update.year, month=to_update.month, day=to_update.day) ##Trouble shoot for working between Years and Months
                self.new_time = check_time.repl_date(to_replace, add_days)  ###FINISH THIS LINE
            else:
                self.new_time =check_time.repl_date(datetime.strptime(wtime, '%H:%M'))  ###FINISH THIS LINE
                print(self.new_time)

            if show != 0: print('Check Time results: {}{} becomes {}'.format(self.date, time, self.new_time))

    def __repr__(self):
        print(self.new_time)
        return '{}'.format(self.new_time)


    @staticmethod
    def repl_date(item, add_days=0, show=0):
        print("Print item {} -> {}".format(item, item.day))
        new_item = item.replace(year=item.year, month=item.month, day=item.day)
        item = new_item + timedelta(days=add_days)
        if show != 0: print("Old: {} ==> New: {}".format(item, new_item))
        return item


class Travel:
    def __init__(self, to_set=None, from_set=None, kms=None):
        self.to_set = to_set
        self.from_set = from_set
        self.kms=kms

    def __repr__(self):
        if self.to_set or self.from_set:
            return "To Set: {} From Set: {}".format(self.to_set, self.from_set)
            # return {'to_set': self.to_set, 'from_set':self.from_set}
        else:
            return '[N/A]'

class Hours:
    def __init__(self, start=None, crew=None, wrap=None, travel=None):
        self.start=start
        self.crew=crew
        self.wrap=wrap
        self.travel=travel

    def __repr__(self):
        return "Start: {} Crew: {} Wrap: {} \n[Travel] {}".format(self.start, self.crew, self.wrap, self.travel)


class Lunch:
    def __init__(self, date=None, start=None, end=None):
        self.date = date
        self.start=start
        self.end=end
        self.total_time=None

        if self.date:
            print('Start: {} End:{} Date:{}'.format(self.start, self.end, self.date))
            self.start = check_time(time=start, date=self.date)  # save date in here as well for math
            self.end = check_time(time=end, date=self.date)  # save date in here as well for math

            self.date=datetime.strptime(date, '%Y-%m-%d')
            # new_start= datetime.strptime(self.start, '%H:%M')
            self.start=self.start.new_time.replace(year=self.date.year, month=self.date.month, day=self.date.day)
            self.end=self.end.new_time.replace(year=self.date.year, month=self.date.month, day=self.date.day)
            ##Changing to String
            # new_start = self.start.new_time.strftime('%H:%M')
            new_start = self.start.strftime('%H:%M')
            new_end=self.end.strftime('%H:%M')
            ##Changing to String
            # self.start=new_start.replace(year=self.date.year, month=self.date.month, day=self.date.day)
            # self.end=new_end.replace(year=self.date.year, month=self.date.month, day=self.date.day)
            # self.total_time = self.end.new_time - self.start.new_time
            self.total_time = self.end - self.start

            # self.start=self.start.new_time.strftime('%H:%M')
            # self.end=self.end.new_time.strftime('%H:%M')

    def __repr__(self):
        if self.date:
            return "{}-{}".format(self.start.strftime('%H:%M'), self.end.strftime('%H:%M'))
        else:
            return "{}-{}".format(self.start, self.end)

class Meals:
    def __init__(self, ndb=None, lunch_1=None, lunch_2=None):
        self.ndb=ndb
        self.meal_1=lunch_1
        self.meal_2=lunch_2

    def __repr__(self):
        return "NDB: {} Meal 1: {} Meal 2: {}".format(self.ndb, self.meal_1, self.meal_2)

class Sheet:
    def __init__(self, date=None, hours=None, meals=None):
        self.date=mod_date(date)
        self.hours=hours
        self.meals=meals
        # Meals
        self.ndb=meals.ndb
        self.meal_1=meals.meal_1
        self.meal_2=meals.meal_2
        #
        # if self.date:
        #     self.date=datetime.strptime(date, '%Y-%m-%d')
        #     self.date=self.date.strftime('%Y-%m-%d')


    def __repr__(self):
        temp_sheet=[self.date, self.hours, self.meals]
        print('\n\nResults: {}\n'.format(temp_sheet))
        return "[Date] {} \n[Hours] {} \n[Meals] {}".format(self.date, self.hours, self.meals)

Date='2018-01-17'


# lunch_1=Lunch(date=Date,start='26:15', end='26:45')

lunch_1=Lunch()
lunch_2=Lunch()

travel_time=Travel(to_set=':20', from_set=':20')
temp=[]
temp.append(Sheet(Date, Hours(start='09:00', crew='09:00', wrap='28:00',travel=travel_time), Meals(lunch_1=lunch_1, lunch_2=lunch_2)))

sheet_keys = [
    'date',
    'start',
    'crew_call',
    'wrap',
    'travel',
    'ndb',
    'meals'
]

time_keys = [
    'start',
    'end'
]

print(temp)
print(temp[0].meals.meal_1.date)

