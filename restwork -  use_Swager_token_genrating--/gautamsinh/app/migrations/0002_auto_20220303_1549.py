# Generated by Django 3.0.7 on 2022-03-03 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='catid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='app.Category'),
        ),
    ]
