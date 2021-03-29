from django.contrib import admin
from decore.models import Pais
from decore.models import Barrio
from decore.models import Empresa
from decore.models import Profesion
from decore.models import Ocupacion
from decore.models import Municipio
from decore.models import Integrante
from decore.models import Departamento
from decore.models import TipoSociedad
from decore.models import NivelEstudio
from decore.models import ModeloNegocio
from decore.models import EtapaProyecto
from decore.models import TamanioEmpresa
from decore.models import ActividadEconomica
from decore.models import DivisionTerritorial
from decore.models import ProyectoEmpresarial
from decore.models import InformacionContactoEmpresa
from decore.models import ProyectoEmpresarialIntegrante
from import_export.admin import ImportExportModelAdmin
from django.db.models import Count

class PaisAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
        
class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    
class InformacionContactoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'instagram', 'facebook', 'pais', 'departamento', 'municipio', 'direccion')
        
class MunicipioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
        
class DivisionTerritorialAdmin(admin.ModelAdmin):
    pass
    
class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    
class TamanioEmpresaAdmin(admin.ModelAdmin):
    pass
    
class ActividadEconomicaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    
class TipoSociedadAdmin(admin.ModelAdmin):
    pass
    
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nit', 'razon_social', 'tamanio_empresa', 
        'tipo_sociedad', 'actividad_economica', 'integrante_count')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _integrante_count = Count('integrante', distinct=True)
        )
        return queryset

    def integrante_count(self, obj):
        return obj._integrante_count
    
class ProfesionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    
class OcupacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cargo', 'ocupacion', 'nivel_estudio', 'empresa',
        'es_lider', 'edad', 'sexo')
    
class NivelEstudioAdmin(admin.ModelAdmin):
    pass
    
class EtapaProyectoAdmin(admin.ModelAdmin):
    pass
    
class ProyectoEmpresarialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'etapa_proyecto', 'empresa', 'proyectoempresarialintengrante_count')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _proyectoempresarialintegrante_count = Count('proyectoempresarialintegrante', distinct=True)
        )
        return queryset
        
    def proyectoempresarialintengrante_count(self, obj):
        return obj._proyectoempresarialintegrante_count
        
class ProyectoEmpresarialIntegranteAdmin(admin.ModelAdmin):
    list_display = ('proyecto_empresarial', 'integrante')
    
class ModeloNegocioAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'quien_ayudara', 'que_haces', 'a_quien_ayudas')
        
admin.site.register(Pais, PaisAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(InformacionContactoEmpresa, InformacionContactoEmpresaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(DivisionTerritorial, DivisionTerritorialAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(TamanioEmpresa, TamanioEmpresaAdmin)
admin.site.register(ActividadEconomica, ActividadEconomicaAdmin)
admin.site.register(TipoSociedad, TipoSociedadAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Profesion, ProfesionAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(NivelEstudio, NivelEstudioAdmin)
admin.site.register(EtapaProyecto, EtapaProyectoAdmin)
admin.site.register(ProyectoEmpresarial, ProyectoEmpresarialAdmin)
admin.site.register(ProyectoEmpresarialIntegrante, ProyectoEmpresarialIntegranteAdmin)
admin.site.register(ModeloNegocio, ModeloNegocioAdmin)
