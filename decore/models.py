# Python ORM
from django.db import models

# Utilities
import uuid
from import_export import resources
from django.core.validators import MaxLengthValidator
from django.core.validators import URLValidator
from django.core.validators import EmailValidator

# Empresa y relaciones externas
class TamanioEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = 'Tamaño de empresas'
    
class TipoSociedad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = 'Tipos de sociedades'

class ActividadEconomica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Actividades económicas'
        
class Empresa(models.Model):
    LOCAL = 'L'
    REGIONAL = 'R'
    NACIONAL = 'N'
    MULTINACIONAL = 'M'
    CUBRIMIENTO_CHOICES = [
        (LOCAL, 'Local'),
        (REGIONAL, 'Regional'),
        (NACIONAL, 'Nacional'),
        (MULTINACIONAL, 'Multinacional'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nit = models.CharField(max_length=10, unique=True)
    razon_social = models.CharField(max_length=30)
    fecha_formalizacion = models.DateField(max_length=30)
    tamanio_empresa = models.ForeignKey(TamanioEmpresa, null=True, on_delete=models.SET_NULL)
    tipo_sociedad = models.ForeignKey(TipoSociedad, null=True, on_delete=models.SET_NULL)
    actividad_economica = models.ForeignKey(ActividadEconomica, null=True, on_delete=models.SET_NULL)
    cubrimiento = models.CharField(
        max_length=2,
        choices = CUBRIMIENTO_CHOICES,
        default = LOCAL
    )
    cantidad_empleados = models.PositiveIntegerField(default=0)
    productos = models.CharField(max_length=1000, null=True)
    servicios = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.razon_social
    
class ModeloNegocio(models.Model):
    empresa = models.OneToOneField(
        Empresa, 
        on_delete=models.CASCADE,
        primary_key=True
    )
    quien_ayudara = models.CharField(max_length=1000)
    como_hace = models.CharField(max_length=1000)
    que_haces = models.CharField(max_length=1000)
    como_interactuas = models.CharField(max_length=1000)
    a_quien_ayudas = models.CharField(max_length=1000)
    que_necesitas = models.CharField(max_length=1000)
    como_alcanzarlos = models.CharField(max_length=1000)
    cual_sera_costo = models.CharField(max_length=1000)
    cuanto_ganaras = models.CharField(max_length=1000)
    
    class Meta:
        verbose_name_plural = 'Modelos de negocios'
    
# Informacion de contacto empresa relaciones externas de informacion_contacto_empresa
class Pais(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Paises'
    
class Departamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        ordering = ['nombre']
    
class Municipio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        ordering = ['nombre']
    
class DivisionTerritorial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Divisiones territoriales'
    
class Barrio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        ordering = ['nombre']

class InformacionContactoEmpresa(models.Model):
    empresa = models.OneToOneField(
        Empresa, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    celular = models.PositiveIntegerField(unique=True)
    celular2 = models.PositiveIntegerField(unique=True, null=True)
    telefono = models.PositiveIntegerField(unique=True, null=True)
    correo_electronico = models.EmailField(validators=[EmailValidator('Email invalid')], unique=True, null=True)
    instagram = models.URLField(validators=[URLValidator()], unique=True, null=True)
    facebook = models.URLField(validators=[URLValidator()], unique=True, null=True)
    pais = models.ForeignKey(Pais, null=True, on_delete=models.SET_NULL)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL)
    municipio = models.ForeignKey(Municipio, null=True, on_delete=models.SET_NULL)
    division_territorial = models.ForeignKey(DivisionTerritorial, null=True, on_delete=models.SET_NULL)
    barrio = models.ForeignKey(Barrio, null=True, on_delete=models.SET_NULL)
    otro_barrio = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.empresa} - {self.municipio}'
    
    class Meta:
        # db_table = 'decore_informacion_contacto_empresa'
        indexes = [
            models.Index(fields=['celular'], name='celular_idx'),
            models.Index(fields=['celular2'], name='celular2_idx'),
            models.Index(fields=['telefono'], name='telefono_idx'),
            models.Index(fields=['correo_electronico'], name='correo_electronico_idx'),
        ]
    
# Integrante y relaciones externas
class Profesion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Profesiones'
    
class Ocupacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = 'Ocupaciones'
    
class NivelEstudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = 'Niveles de estudio'
        
class Integrante(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),   
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre_completo = models.CharField(max_length=80)
    cargo = models.CharField(max_length=30)
    profesion = models.ForeignKey(Profesion, null=True, on_delete=models.SET_NULL)
    ocupacion = models.ForeignKey(Ocupacion, null=True, on_delete=models.SET_NULL)
    nivel_estudio = models.ForeignKey(NivelEstudio, null=True, on_delete=models.SET_NULL)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(
        max_length=2,
        choices = GENDER_CHOICES,
        default = MALE
    )
    es_lider = models.BooleanField(default=False)
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre_completo} - {self.cargo}'
    
# Proyecto empresarial y relaciones externas
class EtapaProyecto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = 'Etapas de proyectos'
    
class ProyectoEmpresarial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(null=False)
    etapa_proyecto = models.ForeignKey(EtapaProyecto, null=True, on_delete=models.SET_NULL)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False, null=False)
    facturacion_mensual_aprox = models.PositiveIntegerField(default=0)
    tipo_mercado = models.CharField(max_length=5, null=True)
    numero_integrantes = models.PositiveIntegerField(default=0)
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = 'Proyectos empresariales'
    
class ProyectoEmpresarialIntegrante(models.Model):
    proyecto_empresarial = models.ForeignKey(ProyectoEmpresarial, null=False, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Integrante, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.proyecto_empresarial} {self.integrante}'
    
    class Meta:
        unique_together = ['proyecto_empresarial', 'integrante']
