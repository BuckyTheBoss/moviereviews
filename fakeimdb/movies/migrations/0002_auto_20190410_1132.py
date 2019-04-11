# Generated by Django 2.2 on 2019-04-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='small_img',
        ),
        migrations.AddField(
            model_name='movie',
            name='big_img',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
