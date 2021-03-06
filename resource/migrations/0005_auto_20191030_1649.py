# Generated by Django 2.2.6 on 2019-10-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_server_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='idc',
            name='zbgroupid',
            field=models.IntegerField(blank=True, help_text='zabbix群组id', null=True, verbose_name='zabbix群组id'),
        ),
        migrations.AddField(
            model_name='server',
            name='zbhostid',
            field=models.IntegerField(blank=True, help_text='zabbix主机id', null=True, verbose_name='zabbix主机id'),
        ),
    ]
