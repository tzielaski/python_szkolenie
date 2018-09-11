from datetime import datetime, timezone

date1 = 'April 12, 1961 2:07 local time'  # ALMT Timezone
date2 = '"07/21/69 2:56:15 AM UTC"'

date1 = date1.replace(' local time', '')
datetime1 = datetime.strptime(date1, '%B %d, %Y %H:%M')
datetime2 = datetime.strptime(date2, '"%m/%d/%y %I:%M:%S %p %Z"')

print(datetime1.isoformat())
print(datetime2.isoformat())

duration = datetime2 - datetime1
print(duration)

past_moment = datetime.utcnow() - duration
print(f'What happened on {past_moment:%Y-%m-%d %H:%M}?')
