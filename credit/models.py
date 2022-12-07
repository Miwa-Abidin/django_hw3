from django.db import models

from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО')
    citizenship = models.CharField(max_length=20, default='Кыргызстан', verbose_name='гражданство')
    birth_year = models.DateField(verbose_name='Год рождения')
    work_place = models.CharField(max_length=20, verbose_name='Место работы', null=True, blank=True)
    update_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

class Account(models.Model):
    number = models.CharField(max_length=16, verbose_name='номер аккаунта')
    account_type = models.IntegerField(default=1, verbose_name='тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        db_table = 'Accounts'
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return f'{self.number}-{self.account_type}-{self.client}'

class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateField(auto_now=timezone)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')

    class Meta:
        db_table = 'Loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return f'{self.sum} - {self.date} - {self.account}'
