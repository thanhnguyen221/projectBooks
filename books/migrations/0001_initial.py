# Generated by Django 5.1 on 2024-08-30 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_sach', models.CharField(max_length=200)),
                ('tac_gia', models.CharField(max_length=100)),
                ('ngay_xuat_ban', models.DateField()),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('anh_bia', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Chuong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_chuong', models.CharField(max_length=200)),
                ('so_chuong', models.PositiveIntegerField()),
                ('noi_dung', models.TextField()),
                ('sach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chuong', to='books.sach')),
            ],
        ),
    ]
