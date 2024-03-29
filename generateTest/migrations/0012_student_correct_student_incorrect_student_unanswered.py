# Generated by Django 4.0.6 on 2023-04-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateTest', '0011_questions_q_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='correct',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='incorrect',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='unanswered',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
