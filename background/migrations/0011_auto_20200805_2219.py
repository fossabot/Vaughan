# Generated by Django 3.0.8 on 2020-08-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0010_auto_20200805_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(default='untaged', max_length=200),
        ),
    ]
