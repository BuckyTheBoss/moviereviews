# Generated by Django 2.2 on 2019-04-11 05:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190410_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewcomment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]