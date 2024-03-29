# Generated by Django 5.0.3 on 2024-03-19 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('seccion', models.TextField()),
                ('hInicio', models.TimeField(db_column='h_inicio')),
                ('hFinal', models.TimeField(db_column='h_final')),
            ],
            options={
                'db_table': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('especializacion', models.TextField()),
                ('telefono', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'docentes',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('pc1', models.FloatField()),
                ('pc2', models.FloatField()),
                ('pc3', models.FloatField()),
                ('examenFinal', models.FloatField(db_column='examen_final')),
                ('promedio', models.FloatField()),
                ('cursoId', models.ForeignKey(db_column='curso_id', on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
            ],
            options={
                'db_table': 'calificaciones',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='docenteId',
            field=models.ForeignKey(db_column='docente_id', on_delete=django.db.models.deletion.CASCADE, to='colegio.docente'),
        ),
        migrations.CreateModel(
            name='CursoEstudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cursoId', models.ForeignKey(db_column='curso_id', on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
                ('estudianteId', models.ForeignKey(db_column='estudiante_id', on_delete=django.db.models.deletion.CASCADE, to='colegio.estudiante')),
            ],
            options={
                'db_table': 'curso_estudiante',
            },
        ),
    ]
