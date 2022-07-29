import random
import datetime
print(random.randrange(5))
print(random.randrange(5,10))
print(random.randrange(0,10,3))
start_date=datetime.date(2019,2,1)
end_date=datetime.date(2019,3,1)
delta=end_date-start_date
time_days=delta.days
random_day=random.randrange(time_days)
random_date=start_date+datetime.timedelta(days=random_day)
print(random_date)