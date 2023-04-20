# Generated by Django 4.0.6 on 2023-03-23 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generateTest', '0003_remove_student_test_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='test_id',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='Student_test', to='generateTest.test'),
            preserve_default=False,
        ),
    ]