# Generated by Django 5.1.2 on 2024-10-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_sabtmoshaver_adress_sabtmoshaver_adress2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabtmoshaver',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='sabtmoshaver',
            name='jensiyat',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
