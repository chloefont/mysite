# Generated by Django 2.2.10 on 2020-02-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_question_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='solution',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]