# Generated by Django 3.2.19 on 2023-10-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_delete_careermodule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='careerID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
