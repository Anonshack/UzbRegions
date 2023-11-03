# Generated by Django 4.2.5 on 2023-09-15 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UzbRegions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name_uz', models.CharField(max_length=50)),
                ('region_name_en', models.CharField(max_length=50)),
                ('region_name_ru', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'uzb_regions',
            },
        ),
        migrations.CreateModel(
            name='UzbDistricts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name_uz', models.CharField(max_length=50)),
                ('district_name_en', models.CharField(max_length=50)),
                ('district_name_ru', models.CharField(max_length=50)),
                ('district_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_regions.uzbregions')),
            ],
            options={
                'db_table': 'uzb_dictricts',
            },
        ),
    ]
