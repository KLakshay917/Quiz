# Generated by Django 4.0.6 on 2023-04-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateTest', '0010_test_mutli_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='q_req',
            field=models.BooleanField(default=False),
        ),
    ]
