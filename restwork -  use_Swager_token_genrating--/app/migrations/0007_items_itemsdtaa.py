# Generated by Django 3.0.7 on 2022-03-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220308_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='itemsdtaa',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
