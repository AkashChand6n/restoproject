# Generated by Django 4.1.3 on 2025-01-17 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0004_rename_regi_registers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyers',
            name='userpassword',
        ),
    ]
