from django.db import models

class Bouquets(models.Model):
    category = models.CharField('Категория', max_length=40)
    image = models.CharField('Изображение', max_length=40)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

class Orders(models.Model):
    bouquet_id = models.IntegerField('ID Букета')
    name = models.CharField('Имя клиента', max_length=50)
    telephone = models.CharField('Номер телефона', max_length=15)
    adress = models.CharField('Адрес', max_length=100)
    comments = models.CharField('Пожелания к заказу', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказов'