# Generated by Django 4.0.5 on 2022-07-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_remove_book_bk_guest_count_remove_book_bk_hall_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='us_mobile',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='us_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
