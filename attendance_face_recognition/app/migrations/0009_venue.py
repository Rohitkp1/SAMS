# Generated by Django 4.0.4 on 2022-06-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_services_sr_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('vn_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('vn_name', models.CharField(max_length=100)),
                ('vn_address', models.CharField(max_length=100)),
                ('vn_status', models.IntegerField(default=0, max_length=100)),
                ('vn_created_by', models.CharField(default='', max_length=100)),
            ],
        ),
    ]