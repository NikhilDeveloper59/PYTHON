import time
# Used for delays and time tracking.

print(f"start time:{time.time()}")

time.sleep(2) #  Delay / Pause Execution

print(f"end time:{time.time()}") # this will print after 2 second delay

print(f"Current Time in Readable Form:{time.ctime()}")

# print(f"Local Time:{time.localtime()}")
t = time.localtime() 
print("Year:", t.tm_year)
print("Month:", t.tm_mon)
print("Day:", t.tm_mday)
print("Hour:", t.tm_hour)
