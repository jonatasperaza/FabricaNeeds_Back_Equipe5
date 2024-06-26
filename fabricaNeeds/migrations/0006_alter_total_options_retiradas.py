# Generated by Django 5.0.4 on 2024-04-23 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabricaNeeds', '0005_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='total',
            options={'verbose_name': 'Total'},
        ),
        migrations.CreateModel(
            name='Retiradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retirada', models.IntegerField()),
                ('data', models.DateField(auto_now_add=True)),
                ('retirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabricaNeeds.contribuinte')),
            ],
            options={
                'verbose_name': 'Retirada',
                'verbose_name_plural': 'Retiradas',
            },
        ),
    ]
