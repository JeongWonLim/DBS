# Generated by Django 4.0.3 on 2022-04-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addclass',
            name='classname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
