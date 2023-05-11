from . import views
from django.urls import path, include
app_name = 'movieapp'


urlpatterns = [
    path('', views.home, name='home'),

    path('movies/<int:id>', views.detail, name='Detail'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

    path('form', views.form, name='forms'),
]
