from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from preinscripcion.home.views import views, disponibilidadView, doncenteView, materiaView, perfilView


router = routers.DefaultRouter()
router.register(r'count', views.CountViewSet,base_name="count")
router.register(r'especialidades', views.EspecialidadView,base_name="especialidades")
router.register(r'materiasInfo', views.MateriaView,base_name="materiasInfo")
router.register(r'materias', views.MateriaView,base_name="materias")
router.register(r'alumnos', views.AlumnoView,base_name="alumnos")
router.register(r'avance', views.AvanceMateriaView,base_name="avance")
router.register(r'especialidades', views.EspecialidadView,base_name="especialidadview")

router.register(r'materias', materiaView.MateriaViewSet)
router.register(r'docentes', doncenteView.DocenteViewSet)
router.register(r'disponibilidad', disponibilidadView.DisponibilidadViewSet)
router.register(r'perfiles', perfilView.PerfilViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
