from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'), 
    path('edit/<int:pk>/',views.edit,name='edit')
]
