# Generated by Django 3.1.5 on 2021-03-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenewableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cityname', models.CharField(max_length=50)),
                ('wattage', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
