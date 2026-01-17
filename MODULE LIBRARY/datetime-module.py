# Used for date and time.
from datetime import datetime 

current_datetime = datetime.now()
print(current_datetime)

#  customize based on your requirement
print(current_datetime.strftime("Date:%d-%m-%y"))
print(current_datetime.strftime("Time:%H-%M-%S"))
print(current_datetime.strftime("Date:%d-%m-%y  Time:%H-%M-%S"))

print(current_datetime.date())
print(current_datetime.time())




