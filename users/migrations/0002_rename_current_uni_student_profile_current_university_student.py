# Generated by Django 3.2.6 on 2021-08-10 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='current_uni_student',
            new_name='current_university_student',
        ),
    ]
