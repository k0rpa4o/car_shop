# Generated by Django 5.1.3 on 2024-11-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product_card', '0003_remove_product_no_product_orders_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='transmission',
            field=models.CharField(choices=[('mechanics', 'Mechanics'), ('automatic', 'Automatic')], default='mechanics', max_length=10),
        ),
    ]
