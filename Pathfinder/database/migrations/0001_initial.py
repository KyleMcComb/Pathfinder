# Generated by Django 3.2.18 on 2023-03-27 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=200)),
                ('duration', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleID', models.CharField(max_length=7)),
                ('moduleName', models.CharField(max_length=200)),
                ('duration', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='moduleCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.courses')),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.modules')),
            ],
        ),
    ]
