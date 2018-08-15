# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jslab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=64)),
                ('sex', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=50),
        ),
        migrations.AlterField(
            model_name='pphoto',
            name='description',
            field=models.CharField(max_length=20, null='True', default='添加对图片的描述'),
        ),
    ]
