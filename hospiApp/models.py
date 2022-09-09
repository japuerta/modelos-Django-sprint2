from django.db import models

class pacientes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_paciente', max_length=50)
    apellidos = models.CharField('apellidos_paciente', max_length=50)
    fechaNacimiento = models.DateTimeField()
    genero = models.CharField('genero_paciente', max_length=30, null=True)
    direccion = models.CharField('direccion_paciente', max_length=50)
    longitud = models.CharField('longitud_direccion', max_length=50, null=True)
    latitud = models.CharField('latitud_direccion', max_length=50, null=True)
    telefono = models.BigIntegerField('telefono_paciente')
    ciudad = models.CharField ('ciudad_residencia', max_length=50)
    email = models.EmailField('Email', max_length=100, unique=True)
    
    
class medico(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_medico', max_length=50)
    apellidos = models.CharField('apellidos_medico', max_length=50)
    genero = models.CharField('genero_medico', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_medico')
    registroMedico = models.CharField ('Tarjeta_profesional', max_length=50)
    especialidad = models.CharField ('especialidad_medica', max_length=50)
    pacienteId = models.ForeignKey(pacientes, related_name='medico', on_delete=models.CASCADE)


class enfermero(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_enfermero', max_length=50)
    apellidos = models.CharField('apellidos_enfermero', max_length=50)
    genero = models.CharField('genero_enfermero', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_enfermero')
    pacienteId = models.ForeignKey(pacientes, related_name='enfermero', on_delete=models.CASCADE)
    
class auxiliar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_auxiliar', max_length=50)
    apellidos = models.CharField('apellidos_auxiliar', max_length=50)
    genero = models.CharField('genero_auxiliar', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_auxiliar')
    pacienteId = models.ForeignKey(pacientes, related_name='auxiliar', on_delete=models.CASCADE)
    
class acompañante(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_acompañante', max_length=50)
    apellidos = models.CharField('apellidos_acompañante', max_length=50)
    genero = models.CharField('genero_enfermero', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_enfermero')
    email = models.EmailField('Email', max_length=100, unique=True)
    pacienteId = models.ForeignKey(pacientes, related_name='acompañante', on_delete=models.CASCADE)
    
class historia_clinica(models.Model):
    id = models.AutoField(primary_key=True)
    diagnosticos = models.CharField('diagnostico', max_length=30)
    signos = models.CharField('signos', max_length=30)
    oximetria = models.CharField('oximetria', max_length=30)
    FrecRespiratoria = models.CharField('frecuencia_respiratoria', max_length=30)
    FrecCardiaca = models.CharField('frecuencia_cardiaca', max_length=30)
    Temperatura = models.CharField('temperatura', max_length=30)
    presionArterial = models.CharField('presion_arterial', max_length=30)
    glicemias = models.CharField('glicemias', max_length=30)
    sugerencias_cuidado = models.CharField('sugerencias_cuidado', max_length=300)
    pacienteId = models.ForeignKey(pacientes, related_name='historia_clinica', on_delete=models.CASCADE)


