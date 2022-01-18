# Generated by Django 4.0.1 on 2022-01-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='bio',
            field=models.TextField(default='Bio pending'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(default='Male', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='species',
            field=models.CharField(default='Dog', max_length=50),
            preserve_default=False,
        ),
    ]
