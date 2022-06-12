from django.urls import path
from todo_app import views



urlpatterns = [

    path('', views.home, name='home' ),
    path('edit/<id>', views.edit, name='edit' ),
    path('delete/<str:pk>', views.delete, name='delete' ),
]
