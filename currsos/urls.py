from django.urls import path
from django.contrib.auth import views as auth_views

from currsos.views import AsignacionView, AsignacionNew, AsignacionEdit, AsignacionDel


urlpatterns = [
    path('asignacion/', AsignacionView.as_view(), name='alumn_list'),
    path('asignacion/new', AsignacionNew.as_view(), name='asignacion_new'),
    path('asignacion/edit/<int:pk>', AsignacionEdit.as_view(), name='asignacion_edit'),
    path('asignacion/delete/<int:pk>', AsignacionDel.as_view(), name='asignacion_del'),
]