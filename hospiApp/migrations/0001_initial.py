# Generated by Django 4.1.1 on 2022-09-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pacientes',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_paciente')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_paciente')),
                ('fechaNacimiento', models.DateTimeField()),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_paciente')),
                ('direccion', models.CharField(max_length=50, verbose_name='direccion_paciente')),
                ('longitud', models.CharField(max_length=50, null=True, verbose_name='longitud_direccion')),
                ('latitud', models.CharField(max_length=50, null=True, verbose_name='latitud_direccion')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_paciente')),
                ('ciudad', models.CharField(max_length=50, verbose_name='ciudad_residencia')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_medico')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_medico')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_medico')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_medico')),
                ('registroMedico', models.CharField(max_length=50, verbose_name='Tarjeta_profesional')),
                ('especialidad', models.CharField(max_length=50, verbose_name='especialidad_medica')),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='hospiApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='historia_clinica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosticos', models.CharField(max_length=30, verbose_name='diagnostico')),
                ('signos', models.CharField(max_length=30, verbose_name='signos')),
                ('oximetria', models.CharField(max_length=30, verbose_name='oximetria')),
                ('FrecRespiratoria', models.CharField(max_length=30, verbose_name='frecuencia_respiratoria')),
                ('FrecCardiaca', models.CharField(max_length=30, verbose_name='frecuencia_cardiaca')),
                ('Temperatura', models.CharField(max_length=30, verbose_name='temperatura')),
                ('presionArterial', models.CharField(max_length=30, verbose_name='presion_arterial')),
                ('glicemias', models.CharField(max_length=30, verbose_name='glicemias')),
                ('sugerencias_cuidado', models.CharField(max_length=300, verbose_name='sugerencias_cuidado')),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_clinica', to='hospiApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='enfermero',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_enfermero')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_enfermero')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_enfermero')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_enfermero')),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enfermero', to='hospiApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='auxiliar',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_auxiliar')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_auxiliar')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_auxiliar')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_auxiliar')),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auxiliar', to='hospiApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='acompañante',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_acompañante')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_acompañante')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_enfermero')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_enfermero')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('pacienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompañante', to='hospiApp.pacientes')),
            ],
        ),
    ]
