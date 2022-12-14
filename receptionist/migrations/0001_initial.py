# Generated by Django 4.0.5 on 2022-11-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('size', models.CharField(choices=[('Executive', 'Executive'), ('Ordinary', 'Ordinary')], max_length=100)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]
