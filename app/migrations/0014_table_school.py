# Generated by Django 4.0.3 on 2022-05-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_quiz_endtime_alter_quiz_starttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studentnum', models.IntegerField()),
                ('classnum', models.IntegerField()),
                ('tel', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
