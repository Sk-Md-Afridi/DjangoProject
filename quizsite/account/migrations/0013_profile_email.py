# Generated by Django 3.1.3 on 2021-07-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210625_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
