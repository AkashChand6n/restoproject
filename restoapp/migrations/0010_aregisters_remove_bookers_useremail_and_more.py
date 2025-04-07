# Generated by Django 4.1.3 on 2025-03-06 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0009_alter_bookers_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='aregisters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfname', models.CharField(max_length=255)),
                ('userlname', models.CharField(max_length=255)),
                ('useremail', models.CharField(max_length=255)),
                ('userphone', models.CharField(max_length=255)),
                ('userpassword', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookers',
            name='useremail',
        ),
        migrations.RemoveField(
            model_name='bookers',
            name='username',
        ),
        migrations.RemoveField(
            model_name='bookers',
            name='userphone',
        ),
        migrations.AddField(
            model_name='bookers',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restoapp.registers'),
        ),
    ]
