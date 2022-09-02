from rest_framework import serializers
from .models import DataRecord, Client


class DataRecordSerializer(serializers.ModelSerializer):
    """ Сериализация данных записи """

    class Meta:
        model = DataRecord
        fields = ('id', 'name_specialist', 'registrarion_date', 'status')

    # def to_representation(self, instance):
    #     representation = super(DataRecordSerializer, self).to_representation(instance)
    #     representation['registrarion_date'] = instance.registrarion_date.strftime("%d.%m.%Y %H:%M:%S")
    #     return representation


class ClientSerializer(serializers.ModelSerializer):
    """ Сериализация данных записи """

    class Meta:
        model = Client
        fields = ('id', 'time', 'phone', 'name_client', 'message_text')


class ClientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('time', 'phone')
