"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib.auth import views as auth_views

from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', auth_views.LoginView.as_view()),
    path('index/', views.index, name='index'),
    path('api/', views.api, name='api'),
    path('users/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]


