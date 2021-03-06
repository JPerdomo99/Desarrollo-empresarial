# Generated by Django 3.1.7 on 2021-03-29 01:31

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('decore', '0004_auto_20210328_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etapaproyecto',
            options={'verbose_name_plural': 'Etapas de proyectos'},
        ),
        migrations.AlterModelOptions(
            name='proyectoempresarial',
            options={'verbose_name_plural': 'Proyectos empresariales'},
        ),
        migrations.AlterField(
            model_name='actividadeconomica',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8204ce9d-af72-4100-a271-e8c63321455b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='barrio',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8df371b1-2361-49c0-9eb4-12c113045cfe'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='id',
            field=models.UUIDField(default=uuid.UUID('74dab07f-9eaa-4fdf-8409-d5e05312b606'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='divisionterritorial',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8583bd79-b97e-4099-b6e3-e973cb707c58'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cubrimiento',
            field=models.CharField(choices=[('L', 'Local'), ('R', 'Regional'), ('N', 'Nacional'), ('M', 'Multinacional')], default='L', max_length=2),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.UUIDField(default=uuid.UUID('67ec88a9-1014-4287-b6f5-bbb528777836'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='etapaproyecto',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3a32167f-a0ce-4d5b-b77a-e850081d490f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='informacioncontactoempresa',
            name='celular2',
            field=models.PositiveIntegerField(null=True, unique=True, validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='informacioncontactoempresa',
            name='correo_electronico',
            field=models.EmailField(max_length=254, null=True, unique=True, validators=[django.core.validators.EmailValidator('Email invalid')]),
        ),
        migrations.AlterField(
            model_name='informacioncontactoempresa',
            name='facebook',
            field=models.URLField(null=True, unique=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='informacioncontactoempresa',
            name='instagram',
            field=models.URLField(null=True, unique=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='informacioncontactoempresa',
            name='telefono',
            field=models.PositiveIntegerField(null=True, unique=True, validators=[django.core.validators.MaxLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='id',
            field=models.UUIDField(default=uuid.UUID('82353da0-edda-4ddd-853d-e372a7dc75c0'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4d219600-6355-4e18-bd55-4ddd1805119b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nivelestudio',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6d84f618-f27e-4b36-a608-d442499a31b4'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4af04559-e1e8-47d7-bb12-012579c0e075'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pais',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a5c5c105-a054-4b1b-b525-2069a2c11991'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aaf45da8-04d4-4b9d-9b64-63d87948cb07'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proyectoempresarial',
            name='id',
            field=models.UUIDField(default=uuid.UUID('67d983e9-63b2-425e-ab36-428723fb675f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proyectoempresarial',
            name='numero_integrantes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tamanioempresa',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4ee97032-99db-403f-b66d-f41c34b75ea8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tiposociedad',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ca306a64-4340-4e28-90b2-922dbf0ddeea'), primary_key=True, serialize=False),
        ),
    ]
