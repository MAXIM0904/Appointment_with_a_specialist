from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class DataRecord(models.Model):
    STATUS_RECORD = [
        ("free", "свободно"),
        ("busy", "занято"),
    ]
    name_specialist = models.CharField(max_length=150, verbose_name="Имя специалиста", default="Иванов Иван Иванович")
    registrarion_date = models.DateTimeField(auto_now=False, verbose_name="Записи")
    status = models.CharField(
        max_length=14, choices=STATUS_RECORD, blank=True, default="free", verbose_name="Статус записи"
    )

    class Meta:
        ordering = ["registrarion_date"]
        verbose_name_plural = "Дата и время записи к специалисту"
        verbose_name = "Запись к специалисту"

    def __str__(self):
        return str(self.registrarion_date.strftime("%d.%m.%Y %H:%M"))


class Client(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '79101111111'. Up to 15 digits allowed."
    )

    time = models.OneToOneField(DataRecord, on_delete=models.CASCADE, related_name="time")
    phone = models.CharField(max_length=15, validators=[phone_regex], verbose_name="Номер телефона клиента", blank=False)
    name_client = models.CharField(max_length=100, blank=False, verbose_name="ФИО клиента")
    message_text = models.TextField(verbose_name="Текст сообщения", blank=True)

    class Meta:
        ordering = ["time"]
        verbose_name_plural = "Записанные клиенты"
        verbose_name = "Записанные клиенты"

    def __str__(self):
        return self.name_client
