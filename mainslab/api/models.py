from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='Имя', unique=True, max_length=200)

    def __str__(self):
        return f'{self.name}'


class Organization(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE,
                                    related_name='organizations')
    name = models.CharField(
        verbose_name='Название организации', max_length=200)
    address = models.TextField(
        verbose_name='Адресс организации', max_length=200)
    fraud_weight = models.IntegerField(verbose_name='Уровень жульничества')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'client_name'],
                                    name='unique_org_name_client_name')
        ]

    def __str__(self):
        return f'{self.name}'


class Bills(models.Model):
    clinet_name = models.ForeignKey(Client, on_delete=models.CASCADE,
                                    related_name='bills')
    client_org = models.ForeignKey(Organization, on_delete=models.CASCADE,
                                   verbose_name='Название организации',
                                   max_length=200,related_name='bills')
    check_number = models.IntegerField(verbose_name='Номер счета')
    check_sum = models.IntegerField(verbose_name='Сумма счета')
    date = models.DateTimeField(verbose_name='Дата счета')
    service = models.CharField(verbose_name='Услуга', max_length=200)
    fraud_score = models.IntegerField(verbose_name='Оценка мошенничества')
    service_class = models.IntegerField(verbose_name='Класс услуги')
    service_name = models.CharField(
        verbose_name='Наименование класса услуги', max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['client_org', 'check_number'],
                                    name='unique_org_check_number')
        ]
