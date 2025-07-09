
from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('create/', views.create_membership, name='create_membership'),
    path('update/<int:pk>/', views.update_membership, name='update_membership'),
    path('delete/<int:pk>/', views.delete_membership, name='delete_membership'),
    path('login/', views.user_login, name='login'),
]
