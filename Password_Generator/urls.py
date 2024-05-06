"""
URL configuration for Password_Generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from Creator.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_page',login_page,name="login"),
    path('signup', signup, name="signup"),
    path('create',create_pass, name='create'),
    path('logout',logout_page, name="logout_page"),
    path('delete_rec/<id>/',delete_rec, name="delete_rec"),
    # path('my_view/', my_view, name="my_view"),
    # path('update_rec/<id>/',update_rec, name="update_rec"),
]
