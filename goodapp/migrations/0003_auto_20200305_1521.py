# Generated by Django 3.0.3 on 2020-03-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0002_auto_20200305_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image174',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='174 image'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image420',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='420 image'),
        ),
    ]
