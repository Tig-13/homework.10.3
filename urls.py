from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Страницы для работы с авторами и цитатами
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quotes/', views.quotes_list, name='quotes_list'),
    path('authors/', views.authors_list, name='authors_list'),
    
    # Авторизация и регистрация
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
