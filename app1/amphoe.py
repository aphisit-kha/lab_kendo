from datetime import datetime

from django.conf import settings

from lab_kendo.utils import generate_id


class Amphoe(object):

    def __init__(self, request):
        self.session = request.session
        if settings.AMPHOE_SESSION_ID not in self.session:
            amphoe = self.session[settings.AMPHOE_SESSION_ID] = []
        else:
            amphoe = self.session.get(settings.AMPHOE_SESSION_ID)
        self.amphoe = amphoe

    def add(self, data=None):
        if len(data) == 0:
            new_row = dict(idno=0, aumpcod='', aumpdes='', postcod='')
        else:
            if 'idno' in data:
                new_row = data
                if new_row['idno'] == '':
                    new_row['idno'] = 0
            else:
                new_row = {**dict(idno=0), **data}
        self.amphoe.append(new_row)
        self.save()
        return new_row

    def update(self, data=None):
        idno = data['idno']
        for item in self.amphoe:
            if idno == item['idno']:
                item.update(data)
                self.save()
                return data

    def save(self):
        self.session.modified = True

    def remove(self, idno):
        for item in self.amphoe:
            if idno == item['idno']:
                index = self.amphoe.index(item)
                del self.amphoe[index]
                self.save()

    def clear(self):
        del self.session[settings.AMPHOE_SESSION_ID]
        self.save()
