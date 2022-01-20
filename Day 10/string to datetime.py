#Using datetime
from datetime import datetime

date_string = 'Jan 27 2011 11:31PM'

datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)

#Using parser
from dateutil import parser

date_time = parser.parse('Jan 27 2011 11:31PM')

print(date_time)
print(type(date_time))
