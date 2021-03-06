# Generated by Django 4.0.3 on 2022-04-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_data_quiz_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='endtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='problemnum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='sqlkeyword',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='starttime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='tablename',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
