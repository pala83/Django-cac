from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('proovedores/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('proovedores/logout/', auth_views.LogoutView.as_view(), name='logout'),    

    path('home/', views.index, name='home'),
    path('cervezas/', views.cervezas, name='cervezas'),
    path('sucursales/', views.index, name='sucursales'),
    path('proovedores/', views.proovedores, name='proovedores'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/<str:nombre>', views.contacto, name='contacto'),
#    path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
#    path('alumnos/detalle/<str:nombre_alumno>', views.alumno_detalle, name='alumnos_detalle'),
#    path('alumnos/historico/2017/', views.alumnos_historico_2017, name='alumnos_historico'),
#    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),
#    path('alumnos/activos', views.alumnos_estado, {'estado': 'activo'}, name="alumnos_activos"),
#    path('alumnos/inactivos', views.alumnos_estado, {'estado': 'inactivo'}, name="alumnos_inactivos"),
]