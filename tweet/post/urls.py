from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="post"),
    path('add/', views.add_post,name="add_post"),
    path('<int:post_id>/edit/', views.edit_del_post,name="edit_post"),
    path('register/', views.register,name="register"),
]