# Generated by Django 2.0.2 on 2018-05-26 09:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='deceases.BodyPart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Decease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256, unique=True)),
                ('chronic', models.BooleanField(default=False)),
                ('duration', models.PositiveSmallIntegerField(default=10)),
                ('contagiousness', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('malignancy', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField()),
                ('diagnostics', models.TextField(blank=True, null=True)),
                ('treatment', models.TextField(blank=True, null=True)),
                ('passing', models.TextField(blank=True, null=True)),
                ('recommendations', models.TextField(blank=True, null=True)),
                ('occurrence', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeceaseAgeGapGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='number of people in average to get decease from 10^6')),
                ('age_gap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AgeGap')),
                ('decease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deceases.Decease')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='DeceaseSymptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chances', models.PositiveSmallIntegerField(default=50, validators=[django.core.validators.MaxValueValidator(100)])),
                ('occurrence', models.PositiveIntegerField(default=1)),
                ('decease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deceases.Decease')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDecease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('cured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('decease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='deceases.Decease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientSymptomDecease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_decease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='symptoms', to='deceases.PatientDecease')),
            ],
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=512, unique=True)),
                ('aliases', models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator(flags=re.RegexFlag(32), message='Should countain names separated with coma(spaces are available)', regex='^([\\w ]+ {0,2}, {0,2})*([\\w ]+ {0,2})$')])),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('body_part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='deceases.BodyPart')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='deceases.Symptom')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='patientsymptomdecease',
            name='symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deceases.Symptom'),
        ),
        migrations.AddField(
            model_name='deceasesymptom',
            name='symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deceases.Symptom'),
        ),
        migrations.AddField(
            model_name='decease',
            name='sphere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deceases.Sphere'),
        ),
        migrations.AddField(
            model_name='decease',
            name='symptoms',
            field=models.ManyToManyField(through='deceases.DeceaseSymptom', to='deceases.Symptom'),
        ),
        migrations.AlterUniqueTogether(
            name='deceasesymptom',
            unique_together={('symptom', 'decease')},
        ),
    ]
