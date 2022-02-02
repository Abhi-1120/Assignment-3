# from datetime import *
# from dateutil import *
# from dateutil.tz import *
#
#
# def convert_date_into_cst(timezone, date_time):
#     dt_str = data['manufacturing_date']
#     format = "%Y-%m-%d %H:%M:%S"
#
#     local = datetime.strptime(dt_str, format)
#     from_zone = tz.gettz(timezone)
#     to_zone = tz.gettz('UTC')
#     local = local.replace(tzinfo=from_zone)
#     central = local.astimezone(to_zone)
#     dt_utc_str = central.strftime(format)
#
#     central = datetime.strptime(dt_str, format)
#     from_zone = tz.gettz('UTC')
#     to_zone = tz.gettz(timezone)
#     central = central.replace(tzinfo=from_zone)
#     date_time = central.astimezone(to_zone)
#     return date_time


# def is_expiry():
#     now = datetime.now()
#     current_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
#     expiry_date = data['expiry_date']
#     if expiry_date > current_datetime:
#         return {'message': 'Item gets Expired.'}
