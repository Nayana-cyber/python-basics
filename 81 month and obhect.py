# the strftime() method is used to format the output of the date

#display the name of the month from date object

import datetime

x = datetime.datetime(2018,6,1)

print(x.strftime("%B"))