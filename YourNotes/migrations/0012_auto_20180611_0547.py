# Generated by Django 2.0 on 2018-06-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YourNotes', '0011_auto_20180610_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotes',
            name='high_imp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usernotes',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
