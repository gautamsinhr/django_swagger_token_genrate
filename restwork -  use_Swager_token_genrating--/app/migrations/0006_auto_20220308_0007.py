# Generated by Django 3.0.7 on 2022-03-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220308_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='itemname',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
