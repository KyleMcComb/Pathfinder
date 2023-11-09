# Generated by Django 3.2.19 on 2023-10-06 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('assessmentID', models.IntegerField(primary_key=True, serialize=False)),
                ('assessmentType', models.CharField(max_length=20)),
                ('assessmentWeight', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('careerID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('jobTitle', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('jobDescription', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lecturerID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('lecturerName', models.CharField(default='name', max_length=100)),
                ('lecturerEmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('moduleID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('moduleName', models.CharField(max_length=100)),
                ('moduleSemester', models.IntegerField(default=3)),
                ('moduleDescription', models.CharField(max_length=250)),
                ('moduleLevel', models.IntegerField(default=1)),
                ('moduleWeight', models.IntegerField(default=20)),
                ('careers', models.ManyToManyField(blank=True, to='database.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('pathwayID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pathwayName', models.CharField(max_length=100)),
                ('pathwayLevels', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False)),
                ('studentCurrentLevel', models.IntegerField(default=1)),
                ('studentCurrentSemester', models.IntegerField(default=1)),
                ('currentPathwayMark', models.IntegerField(default=100)),
                ('pathwayID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.pathway')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModule',
            fields=[
                ('studentModuleID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('stuModMark', models.IntegerField(default=100)),
                ('moduleID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.module')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModuleAssesment',
            fields=[
                ('studentModuleAssesmentID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('assesmentMark', models.IntegerField(default=100)),
                ('assessmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.assessment')),
                ('studentModuleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.studentmodule')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInterest',
            fields=[
                ('studentInterestID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('interestName', models.CharField(max_length=100)),
                ('interestImportance', models.IntegerField(default=0)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
            ],
        ),
        migrations.CreateModel(
            name='ModulePathway',
            fields=[
                ('modulePathwayID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('mpCore', models.BooleanField(default=True)),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module')),
                ('pathwayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.pathway')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleLecturer',
            fields=[
                ('moduleLecturerID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('lecturerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.lecturer')),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module')),
            ],
        ),
        migrations.CreateModel(
            name='CareerModule',
            fields=[
                ('careerModuleID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('careerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.career')),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='moduleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module'),
        ),
    ]