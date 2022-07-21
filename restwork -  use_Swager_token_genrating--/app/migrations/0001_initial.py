# Generated by Django 3.0.7 on 2022-03-03 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Restorent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restoname', models.CharField(max_length=10)),
                ('restocity', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('available', models.BooleanField(default=True)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('restoid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Restorent')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='restoid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Restorent'),
        ),
    ]
