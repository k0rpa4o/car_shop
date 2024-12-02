from django.db import models


class Product(models.Model):
    TRANSMISSION_CHOICES = [
        ('Механика', 'Mechanics'),
        ('Автомат', 'Automatic'),
    ]
    DRIVE_CHOICES = [
        ('Передний привод', 'front_wheel_drive'),
        ('Задний привод', 'rear_wheel_drive'),
        ('Полный привод', '4WD'),
    ]
    product_name = models.CharField(max_length=200, null= True) # имя товара
    product_description = models.CharField(max_length=1000, null= True) # описание товара

    transmission = models.CharField(max_length=15, choices=TRANSMISSION_CHOICES, default='Mechanics')# коробка передач
    engine_size = models.FloatField(max_length=5, default=0.0, null=True)# объем двигателя
    drive = models.CharField(max_length=20, choices=DRIVE_CHOICES, default='Задний привод')# привод авто
    power = models.IntegerField(max_length=5, default=0, null=True)# мощность(л.с)
    color = models.CharField(max_length=50, null= True)# цвет

    product_image = models.URLField(null=True) # фото товара
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.00) # цена товара

    def __str__(self):
        return self.product_name