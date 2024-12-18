from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add),
    path('display/<int:num>',views.display),
    path('update/<int:num>',views.update),
    path('delete/<int:num>',views.delete),
]