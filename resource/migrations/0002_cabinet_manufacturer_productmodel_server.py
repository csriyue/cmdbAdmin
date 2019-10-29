# Generated by Django 2.2.6 on 2019-10-29 06:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='机柜名称', max_length=50, verbose_name='机柜名称')),
                ('idc', models.ForeignKey(help_text='所在机房', on_delete=django.db.models.deletion.CASCADE, to='resource.Idc', verbose_name='所在机房')),
            ],
            options={
                'db_table': 'resources_cabinet',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(db_index=True, help_text='厂商名称', max_length=32, verbose_name='厂商名称')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=300, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'resources_manufacturer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(help_text='型号名称', max_length=32, verbose_name='型号名称')),
                ('vendor', models.ForeignKey(help_text='所属制造商', on_delete=django.db.models.deletion.CASCADE, to='resource.Manufacturer', verbose_name='所属制造商')),
            ],
            options={
                'db_table': 'resources_productmodel',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, help_text='UUID', verbose_name='UUID')),
                ('cabinet_position', models.CharField(help_text='机柜内位置', max_length=32, null=True, verbose_name='机柜内位置')),
                ('manage_ip', models.CharField(db_index=True, default=None, help_text='管理IP', max_length=32, verbose_name='管理IP')),
                ('cabinet', models.ForeignKey(help_text='所在机柜', null=True, on_delete=django.db.models.deletion.CASCADE, to='resource.Cabinet', verbose_name='所在机柜')),
                ('idc', models.ForeignKey(help_text='所在机房', null=True, on_delete=django.db.models.deletion.CASCADE, to='resource.Idc', verbose_name='所在机房')),
                ('model_name', models.ForeignKey(default=None, help_text='服务器型号', on_delete=django.db.models.deletion.CASCADE, to='resource.ProductModel', verbose_name='服务器型号')),
            ],
            options={
                'db_table': 'resources_server',
            },
        ),
    ]