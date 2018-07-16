from django.urls import include, path
from . import views

urlpatterns = [
  #/data/
  path('', views.index, name='index'),
  path('dashboard/', views.dashboard, name='dashboard'),

  #/data/71/
   path('<album_id>/', views.detail, name='detail'),
]