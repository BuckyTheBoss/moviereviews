# Generated by Django 2.2 on 2019-04-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190410_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]