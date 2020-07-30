# Generated by Django 2.2.14 on 2020-07-30 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adai_api', '0005_auto_20200729_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='fecha_de_nacimiento',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='genero',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='apellido_estudiante',
            new_name='student_lastname',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='nombre_estudiante',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='materias',
            old_name='nombre_materia',
            new_name='subject_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default='2020-01-01'),
        ),
    ]