# Generated by Django 4.0.5 on 2022-07-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_category_ct_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bk_booking_status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
