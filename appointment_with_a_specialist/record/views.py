from datetime import datetime, timedelta
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from .models import DataRecord, Client
from .serializers import DataRecordSerializer, ClientSerializer
from . import utils


class CreateRecord(CreateAPIView, utils.UpdateMixin):
    """Класс создания записи"""
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        dict_record = super().post(request, *args, **kwargs)
        self.update_data_record(index=dict_record.data['time'])
        return dict_record


class AllRecord(ListAPIView):
    """Класс возвращает все записи в соответствии с фильтром"""
    permission_classes = (AllowAny,)
    serializer_class = DataRecordSerializer


    def get_queryset(self):
        startdate, enddate = utils.defining_parameters(self)
        queryset = DataRecord.objects.filter(registrarion_date__range=[startdate, enddate])
        return queryset


class DeleteRecord(DestroyAPIView, utils.UpdateMixin):
    """Класс удаления записи"""
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = Client.objects.filter(time_id=self.request.POST['time'], phone=self.request.POST['phone'])
        return queryset


    def delete(self, request, *args, **kwargs):
        dict_record = super(DeleteRecord, self).delete(request, *args, **kwargs)
        self.update_status_free(index=request.POST['time'])
        return dict_record