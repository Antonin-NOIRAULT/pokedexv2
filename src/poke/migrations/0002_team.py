# Generated by Django 4.1.3 on 2022-12-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]