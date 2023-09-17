from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('cervezas/', views.index, name='cervezas'),
    path('sucursales/', views.index, name='sucursales'),
    path('nosotros/', views.index, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/<str:nombre>', views.contacto, name='contacto'),
#    path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
#    path('alumnos/detalle/<str:nombre_alumno>', views.alumno_detalle, name='alumnos_detalle'),
#    path('alumnos/historico/2017/', views.alumnos_historico_2017, name='alumnos_historico'),
#    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),
#    path('alumnos/activos', views.alumnos_estado, {'estado': 'activo'}, name="alumnos_activos"),
#    path('alumnos/inactivos', views.alumnos_estado, {'estado': 'inactivo'}, name="alumnos_inactivos"),
]