from django.urls import path

from . import views

app_name='book' 

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<str:pk>', views.update, name='update')
]