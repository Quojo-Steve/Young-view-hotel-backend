# Generated by Django 4.0.5 on 2022-11-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='size',
            field=models.CharField(choices=[('Executive', 'Executive'), ('Ordinary', 'Ordinary'), ('Standard', 'Standard')], max_length=100),
        ),
    ]
