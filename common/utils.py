from datetime import *
from dateutil.tz import *
import pytz
from datetime import timedelta, datetime


def convert_date_into_cst(timezone, dt_str):
    local_time = pytz.timezone(timezone)
    naive_datetime = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    local_datetime = local_time.localize(naive_datetime, is_dst=None)
    utc_datetime = local_datetime.astimezone(pytz.utc)

    cs_time = utc_datetime - timedelta(hours=6)
    return cs_time
