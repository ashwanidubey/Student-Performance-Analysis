# Generated by Django 3.0.6 on 2021-02-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBankCM',
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
        migrations.CreateModel(
            name='QuestionBankPL',
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
