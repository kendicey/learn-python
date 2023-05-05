# ctrl + click on modules to check for their functionalities
import calendar
import sys

location = sys.path
print(location)

for i in location:
    print(i)


leapdays = calendar.leapdays(2000, 2050)    # 29/2
print(leapdays)

isitleap = calendar.isleap(2036)
print(isitleap)
