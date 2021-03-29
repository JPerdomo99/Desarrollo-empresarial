# Generated by Django 3.1.7 on 2021-03-26 21:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('decore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TamanioEmpresa',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('c3395ebe-a508-4ef0-947e-1cf74699fca3'), editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='tamaño_empresa',
        ),
        migrations.AlterField(
            model_name='actividadeconomica',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b1bddb92-d128-4369-bb7a-cec4399a66a3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='barrio',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2260a1b8-41bf-4eb4-b7e1-d1557efbc71f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9ad4c5b7-735c-406d-bb00-4c6321367b59'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='divisionterritorial',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d8675b02-b990-43f6-9b77-85a2d52309a9'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.UUIDField(default=uuid.UUID('003a76ad-d63b-47f8-b3ec-1d5a8a63a58b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='etapaproyecto',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4935363-fc64-48c1-8923-99e08448e6a2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='id',
            field=models.UUIDField(default=uuid.UUID('08a8546b-ef92-435e-9c9d-a483e44406b8'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8c200a62-dbaa-4ad0-891d-c0909f5e5dc0'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nivelestudio',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0ddbf195-168e-4ff2-8c6d-530a735f973a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0b258194-4b7b-432e-ae2e-00a42b1e3bca'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pais',
            name='id',
            field=models.UUIDField(default=uuid.UUID('75244711-b0a5-4043-9eda-733e4fa8c2c8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('34fb1c6d-ea7b-4e5e-a483-d767cefee6c7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proyectoempresarial',
            name='id',
            field=models.UUIDField(default=uuid.UUID('707e2c53-8bcc-402a-94a0-33756a590d3f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tiposociedad',
            name='id',
            field=models.UUIDField(default=uuid.UUID('69d260a2-f78f-4e2c-9280-872ea4894037'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='TamañoEmpresa',
        ),
        migrations.AddField(
            model_name='empresa',
            name='tamanio_empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='decore.tamanioempresa'),
        ),
    ]
