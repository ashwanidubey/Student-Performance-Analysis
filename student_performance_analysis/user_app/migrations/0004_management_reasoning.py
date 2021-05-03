# Generated by Django 3.0.6 on 2021-04-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20210219_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('opA', models.CharField(max_length=100)),
                ('opB', models.CharField(max_length=100)),
                ('opC', models.CharField(max_length=100)),
                ('opD', models.CharField(max_length=100)),
                ('answerA', models.CharField(max_length=100)),
                ('answerB', models.CharField(max_length=100)),
                ('answerC', models.CharField(max_length=100)),
                ('answerD', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reasoning',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('opA', models.CharField(max_length=100)),
                ('opB', models.CharField(max_length=100)),
                ('opC', models.CharField(max_length=100)),
                ('opD', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]