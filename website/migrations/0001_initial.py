# Generated by Django 4.1.4 on 2022-12-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('variable', models.IntegerField(default=0, primary_key=True, serialize=False)),
            ],
        ),
    ]
