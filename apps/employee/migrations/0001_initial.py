# Generated by Django 2.1.3 on 2018-11-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('email', models.EmailField(max_length=30, verbose_name='邮箱')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='入职日期')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '姓名',
                'verbose_name_plural': '姓名',
            },
        ),
    ]