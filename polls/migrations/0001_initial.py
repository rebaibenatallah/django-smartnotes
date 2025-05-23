# Generated by Django 5.2.1 on 2025-05-10 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='poll_option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('voter_n', models.BigIntegerField()),
                ('Id_poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='voters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('Id_poll_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll_option')),
            ],
        ),
    ]
