# Generated by Django 2.2.5 on 2020-01-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True)),
                ('shop_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('rest_date', models.CharField(blank=True, max_length=100, null=True)),
                ('parking_info', models.CharField(blank=True, max_length=100, null=True)),
                ('img_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'shop',
                'managed': False,
            },
        ),
    ]
