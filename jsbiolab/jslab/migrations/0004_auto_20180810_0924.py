# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jslab', '0003_auto_20180809_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=64)),
                ('sex', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='userInfor2',
        ),
    ]
