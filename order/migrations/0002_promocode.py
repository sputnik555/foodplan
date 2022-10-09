# Generated by Django 4.1.2 on 2022-10-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('promocode', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('discount', models.PositiveIntegerField(verbose_name='Скидка в процентах')),
            ],
        ),
    ]
