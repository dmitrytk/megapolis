from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models

from api.managers import MyUserManager


class Position(Enum):
    """Должности"""
    ADMIN = 'ADMIN'
    EXECUTIVE = 'EXECUTIVE'
    MANAGER = 'MANAGER'
    SENIOR = 'SENIOR'
    MIDDLE = 'MIDDLE'
    JUNIOR = 'JUNIOR'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


# МОДЕЛИ
class Organization(models.Model):
    """Модель для представления как заказчиков так и подрядчиков"""

    name = models.CharField(max_length=70, blank=False)
    type = models.CharField(max_length=70, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    # Различные данные организации
    custom_data = JSONField()

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    """Единая модель Пользователя для аутентификации и контрактов"""

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    # Должность в организации
    position = models.CharField(max_length=255, choices=Position.choices())
    organization = models.ForeignKey(Organization, related_name='organization', on_delete=models.CASCADE)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'organization']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contract(models.Model):
    number = models.CharField(max_length=90, blank=False)
    content = models.TextField(blank=False)
    client = models.ForeignKey(Organization, related_name='client', on_delete=models.CASCADE)
    contractor = models.ForeignKey(Organization, related_name='contractor', on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class ContractEmployee(models.Model):
    """Модель для связи пользователей и договоров. ManyToMany"""

    contract = models.ForeignKey(Contract, related_name='contract', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE)
    # Должность по контракту
    position = models.CharField(max_length=255, choices=Position.choices())

    class Meta:
        unique_together = [['contract', 'employee']]

    def __str__(self):
        return f'{self.employee} {self.contract}'


# ПРЕДСТАВЛЕНИЯ
class ContractView(models.Model):
    """Вью для представления данных контракта, совместно с данными организаций"""
    number = models.CharField(max_length=255)
    content = models.TextField()
    client = models.CharField(max_length=255)
    contractor = models.CharField(max_length=255)
    client_id = models.IntegerField()
    contractor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_contract_view'
