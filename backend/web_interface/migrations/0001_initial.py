# Generated by Django 5.0.2 on 2024-05-21 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Орган')),
            ],
            options={
                'verbose_name': 'Орган',
                'verbose_name_plural': 'Органы',
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата')),
                ('organ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Organs', to='web_interface.organ', verbose_name='Орган')),
            ],
            options={
                'verbose_name': 'Жалоба',
                'verbose_name_plural': 'Жалобы',
            },
        ),
    ]
