# Generated by Django 5.0.3 on 2024-04-03 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='cycle date')),
                ('cycle', models.CharField(choices=[('E', 'Eggs Layed'), ('H', 'Eggs Hatched'), ('C', 'Chrysalis(pupa)'), ('A', 'Adulthood')], default='E', max_length=1)),
                ('butterfly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.butterfly')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
