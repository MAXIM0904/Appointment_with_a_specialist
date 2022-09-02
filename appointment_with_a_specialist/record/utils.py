from .models import DataRecord
from datetime import datetime, timedelta


class UpdateMixin:
    def update_data_record(self, index):
        obj = DataRecord.objects.get(id=index)
        obj.status = 'busy'
        obj.save()
        return True

    def update_status_free(self, index):
        obj = DataRecord.objects.get(id=index)
        obj.status = 'free'
        obj.save()
        return True


def defining_parameters(self):
    """Функция определения даты начала и окончания периода"""
    startdate = datetime.now()
    enddate = startdate + timedelta(days=30)
    if 'start_date' in self.request.data:
        startdate = datetime.strptime(self.request.data['start_date'], '%Y-%m-%d')
        enddate = datetime.strptime(self.request.data['end_date'], '%Y-%m-%d') + timedelta(days=1)
    return startdate, enddate