# Generated by Django 4.1.7 on 2023-12-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_statistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date of this statistics event'),
        ),
    ]
