# Generated by Django 5.0.3 on 2024-04-01 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_attendance_class_day_faculty_delete_book_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Students',
        ),
    ]
