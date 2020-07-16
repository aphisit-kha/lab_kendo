from datetime import datetime


def generate_id(id):
    date = datetime.today()
    slug = '%02i%02i%02i%06i%i' % (
        date.hour, date.minute, date.second, date.microsecond, id
    )
    return int(slug)