import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
json_data = {'time': "2022-02-02 00:24:00"}
utc = datetime.datetime.strptime(json_data['time'], "%Y-%m-%d %H:%M:%S")
utc = utc.replace(tzinfo=from_zone)
cst = utc.astimezone(to_zone)
print(utc)
print(cst)