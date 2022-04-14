# Generated by Django 2.2.5 on 2019-10-13 19:20

import data_app.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashout',
            fields=[
                ('cashout_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Cashout ID')),
                ('client', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('lp', models.IntegerField(verbose_name='LP')),
                ('rate', models.IntegerField()),
                ('profit', models.BigIntegerField()),
                ('lp_type', models.CharField(choices=[('Guristas', 'Guristas'), ('Sanshas', 'Sanshas'), ('DED', 'DED'), ('None', 'None')], max_length=100, verbose_name='LP Type')),
                ('items', django.contrib.postgres.fields.jsonb.JSONField(default=data_app.models.json_default)),
            ],
            options={
                'verbose_name': 'LP Cashout',
                'ordering': ['-cashout_id'],
            },
        ),
    ]