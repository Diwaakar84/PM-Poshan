# Generated by Django 4.1.7 on 2023-02-15 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_last_login_remove_student_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
    ]
