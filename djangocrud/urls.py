
from django.contrib import admin
from django.urls import path
from mapa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('mapa/', views.mapa, name='mapa'),
    path('actualizar-tarea/', views.actualizar_tarea, name='actualizar_tarea'),
    path('eliminar_tarea/', views.eliminar_tarea, name='eliminar_tarea'),
]


# Esto solo debe usarse en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)