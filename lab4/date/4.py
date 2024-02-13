import datetime

x = datetime.datetime(2020, 5, 15, 5, 10, 20)
y = datetime.datetime.now()

difference_in_minutes = (y - x).total_seconds() / 60

print(int(difference_in_minutes))
