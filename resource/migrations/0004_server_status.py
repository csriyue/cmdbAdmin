# Generated by Django 2.2.6 on 2019-10-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0003_remove_server_cabinet_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='status',
            field=models.CharField(db_index=True, help_text='服务器状态', max_length=32, null=True, verbose_name='服务器状态'),
        ),
    ]