"""
URL configuration for IdentityServerApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from identityServerApp import views  # Import views from a different directory
urlpatterns = [
    path('admin/', admin.site.urls),
    path('IdentityServerApi/', include('IdentityServerApi.urls')),  # Replace 'yourappname' with your actual app name

    path('signup/', views.signup, name='signup'), 
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('roles/', views.roles, name='roles'),
    # Add other URL patterns as needed
]