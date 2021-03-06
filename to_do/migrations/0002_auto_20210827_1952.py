# Generated by Django 3.2.6 on 2021-08-27 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='text',
        ),
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
