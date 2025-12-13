# Exercise 2

import time

timestamp = time.strftime("%H:%M:%S")

print(timestamp)

if timestamp < "12:00:00":
    print("Good Morning Sir..")

elif timestamp > "12:00:00" and timestamp < "16:00:00":
    print("Good Afternoon Sir..")

elif timestamp > "16:00:00" and timestamp < "20:00:00":
    print("Good Evening Sir..")
    
else:
    print('Good Night Sir..')