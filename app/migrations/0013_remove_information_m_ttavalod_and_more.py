# Generated by Django 5.1.2 on 2024-11-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_information_m_emtiyaz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information_m',
            name='ttavalod',
        ),
        migrations.AlterField(
            model_name='information_m',
            name='jensiyat',
            field=models.BooleanField(),
        ),
    ]