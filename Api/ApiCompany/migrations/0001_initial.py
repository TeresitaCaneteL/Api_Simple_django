# Generated by Django 3.0.14 on 2022-06-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('tallas', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
