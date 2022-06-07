# Generated by Django 4.0.4 on 2022-06-05 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_group_iscertificateavailable_alter_group_close_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='isClosed',
            field=models.BooleanField(default=False, verbose_name='Жабық па?'),
        ),
        migrations.AlterField(
            model_name='group',
            name='close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 20, 41, 56, 705021), verbose_name='Жабылу уақыты'),
        ),
        migrations.AlterField(
            model_name='group',
            name='isCertificateAvailable',
            field=models.BooleanField(default=False, verbose_name='Курс бітті ма?'),
        ),
    ]