# Generated by Django 4.1.3 on 2025-01-17 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0002_regi_delete_registers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regi',
            name='hashpass',
        ),
    ]
