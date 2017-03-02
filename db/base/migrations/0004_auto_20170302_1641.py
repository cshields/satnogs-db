# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:41
from __future__ import unicode_literals

import db.base.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160504_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telemetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('schema', models.TextField(blank=True)),
                ('decoder', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ['satellite__norad_cat_id'],
                'verbose_name_plural': 'Telemetries',
            },
        ),
        migrations.AlterModelOptions(
            name='demoddata',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='satellite',
            options={'ordering': ['norad_cat_id']},
        ),
        migrations.RemoveField(
            model_name='demoddata',
            name='payload',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='telemetry_decoder',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='telemetry_schema',
        ),
        migrations.AddField(
            model_name='demoddata',
            name='lat',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)]),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='lng',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)]),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='payload_decoded',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='payload_frame',
            field=models.FileField(blank=True, null=True, upload_to=db.base.models._name_payload_frame),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='satellite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telemetry_data', to='base.Satellite'),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='source',
            field=models.CharField(choices=[(b'manual', b'manual'), (b'network', b'network'), (b'sids', b'sids')], default=b'sids', max_length=7),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='station',
            field=models.CharField(default=b'Unknown', max_length=45),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='demoddata',
            name='data_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demoddata',
            name='transmitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Transmitter'),
        ),
        migrations.AddField(
            model_name='telemetry',
            name='satellite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telemetries', to='base.Satellite'),
        ),
        migrations.AddField(
            model_name='demoddata',
            name='payload_telemetry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Telemetry'),
        ),
    ]
