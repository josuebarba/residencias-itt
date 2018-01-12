from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from home.views import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'count',views.CountViewSet,base_name="count")
router.register(r'especialidades',views.EspecialidadView,base_name="especialidades")
router.register(r'materiasInfo',views.MateriaView,base_name="materiasInfo")
router.register(r'materias',views.MateriaView,base_name="materias")
router.register(r'alumnos',views.AlumnoView,base_name="alumnos")
router.register(r'avance',views.AvanceMateriaView,base_name="avance")
router.register(r'especialidades',views.EspecialidadView,base_name="especialidadview")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    # url(r'^pandas/',views.ReadXls),
    url(r'^addMateriasXlsSheet2/',views.addMaterias),


    # url(r'^especialidades/$',views.EspecialidadView.as_view(),name='especialidad_view'),
    # url(r'materiasInfo/',views.MateriaInfoView.as_view(),name='materiaInfo_view'),
    # url(r'materias/',views.MateriaView.as_view(),name='materia_view'),
    # url(r'alumnos/',views.AlumnoView.as_view(),name='alumno_view'),
    # url(r'avance/',views.AvanceMateriaView.as_view(),name='avance_view'),
    url(r'series/',views.getCount,name='getCount_view'),

    url(r'^go/pick/$', views.pick, name='pick_view'),
    url(r'^login/$', views.login, name='login_view'),
    url(r'^logout/$', views.logout, name='logout_view'),
    url(r'^go/post/$', views.materiasPost, name='post_view'),
    url(r'', views.login, name='login_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
