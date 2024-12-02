# Generated by Django 5.1.3 on 2024-11-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product_card', '0006_product_drive_alter_product_transmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='power',
            field=models.IntegerField(default=0, max_length=5, null=True),
        ),
    ]
