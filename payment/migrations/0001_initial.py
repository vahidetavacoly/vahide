# Generated by Django 5.1.2 on 2024-12-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shenase_kharid', models.CharField(max_length=100)),
                ('mablagh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tarikh', models.DateTimeField(auto_now_add=True)),
                ('authority', models.CharField(max_length=200)),
                ('statu', models.CharField(default='موفق', max_length=20)),
            ],
        ),
    ]