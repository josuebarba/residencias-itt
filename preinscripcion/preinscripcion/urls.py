from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from preinscripcion.home import views


router = routers.DefaultRouter()

# Catalogos

router.register(r'areas', views.AreaViewSet)
router.register(r'evidencias', views.EvidenciaViewSet)
router.register(r'especialidades', views.EspecialidadViewSet)

# Modelos Principales

router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'docentes', views.DocenteViewSet)
router.register(r'materias', views.MateriaViewSet)
router.register(r'carreras', views.CarreraViewSet)

# Modelos Secundarios - Relaciones (1,*)

router.register(r'avances', views.AvanceMateriaViewSet)
router.register(r'disponibilidad', views.DisponibilidadViewSet)
router.register(r'perfiles', views.PerfilViewSet)

# Modelos Secundarios - Relaciones (*,*)

router.register(r'alumnos/materias', views.AlumnoMateriaViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
