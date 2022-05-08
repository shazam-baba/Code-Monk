from django.urls import path
from .import views
urlpatterns = [
    path('api/', views.apiOverview, name='api-overview'),
    
    path('api/text-list/', views.textList, name='text-list'),
    path('api/text-upload/', views.textUpload, name='text-upload'),
    path('api/word-search/', views.wordSearch, name='word-search'),
    
    path('api/register-page/', views.register_page, name='register-page'),
    path('api/login-page/', views.login_page, name='login-page'),
    path('api/logout-page/', views.logout_page, name='logout'),
    
]
