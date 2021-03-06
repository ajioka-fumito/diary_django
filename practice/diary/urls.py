from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'), 
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('detail/<int:pk>/',views.detail,name='detail'),
]
