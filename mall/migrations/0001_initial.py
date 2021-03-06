# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 05:44
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='商品ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='编码')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('order', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mall.Classify')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
                'db_table': 'mall_classify',
                'ordering': ['-order'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=256, verbose_name='评价内容')),
                ('reorder', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('is_anonymous', models.BooleanField(default=True, verbose_name='是否匿名')),
                ('score', models.FloatField(default=10.0, verbose_name='商品评分')),
                ('score_deliver', models.FloatField(default=10.0, verbose_name='配送服务分')),
                ('score_package', models.FloatField(default=10.0, verbose_name='快递包装分')),
                ('score_speed', models.FloatField(default=10.0, verbose_name='送货速度分')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '商品评价',
                'verbose_name_plural': '商品评价',
                'db_table': 'mall_product_comment',
                'ordering': ['-reorder'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='商品ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('content', ckeditor.fields.RichTextField(verbose_name='商品描述')),
                ('types', models.SmallIntegerField(choices=[(11, '虚拟商品'), (12, '实物商品')], default=12, verbose_name='商品类型')),
                ('price', models.IntegerField(default=5, verbose_name='销售价（积分）')),
                ('origin_price', models.FloatField(default=0, verbose_name='原价')),
                ('img', models.ImageField(blank=True, max_length=128, null=True, upload_to='%Y%m/product/', verbose_name='商品主图')),
                ('imei', models.CharField(blank=True, max_length=64, null=True, verbose_name='商品编号')),
                ('channel', models.CharField(blank=True, max_length=32, null=True, verbose_name='渠道')),
                ('buy_link', models.CharField(blank=True, max_length=256, null=True, verbose_name='购买链接')),
                ('online_time', models.DateTimeField(blank=True, null=True, verbose_name='定时上线时间')),
                ('offline_time', models.DateTimeField(blank=True, null=True, verbose_name='定时下线时间')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('reorder', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('status', models.SmallIntegerField(choices=[(11, '售卖中'), (12, '已售罄'), (13, '已下架')], default=13, verbose_name='状态')),
                ('sku_count', models.IntegerField(default=0, verbose_name='库存')),
                ('remain_count', models.IntegerField(default=0, verbose_name='剩余')),
                ('view_count', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('score', models.FloatField(default=10.0, verbose_name='商品评分')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('classes', models.ManyToManyField(blank=True, null=True, related_name='classes', to='mall.Classify', verbose_name='分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'mall_product',
                'ordering': ['-reorder'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标签名称')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='标签编码')),
                ('img', models.ImageField(blank=True, max_length=128, null=True, upload_to='tag/', verbose_name='标签主图')),
                ('reorder', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'mall_tag',
                'ordering': ['-reorder'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='mall.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mall.Product', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
