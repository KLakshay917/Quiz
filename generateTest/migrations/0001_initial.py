# Generated by Django 4.0.6 on 2023-03-23 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('marks', models.IntegerField(default=0)),
                ('email_token', models.CharField(max_length=200)),
                ('test_complete', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('duration', models.DurationField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='generateTest.test')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(max_length=100)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='generateTest.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]