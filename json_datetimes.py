import datetime
import json

DATA = {
    "datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456),
    "astronaut": {
        "date": datetime.date(1923, 11, 18),
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": datetime.datetime(1961, 5, 5, 14, 34, 13), "action": "launch"},
        {"datetime": datetime.datetime(1961, 5, 5, 14, 49, 35), "action": "landing"}
    ]
}


class DatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.convert_datetime)

    def convert_datetime(self, args):
        for key, value in args.items():

            if key == "datetime":
                dt = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                args['datetime'] = dt.replace(tzinfo=datetime.timezone.utc)

            elif key == "date":
                dt = datetime.datetime.strptime(value, '%Y-%m-%d')
                args['date'] = dt.date()

            return args


def encoder_datetime(self, obj):
    if isinstance(obj, datetime.datetime):
        return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'
    elif isinstance(obj, datetime.date):
        return f'{obj:%Y-%m-%d}'


json.JSONEncoder.default = encoder_datetime
with open('JSON_datetimes.json','w', encoding='utf-8') as file:
    file.write(json.dumps(DATA))

with open('JSON_datetimes.json', 'r', encoding='utf-8') as file:
    content = file.read()
    out = json.loads(content, cls=DatetimeDecoder)

print(out)
