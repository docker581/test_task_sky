# Generated by Django 3.0.5 on 2021-08-08 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210803_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='body', to='data.Document', verbose_name='Документ'),
        ),
    ]
