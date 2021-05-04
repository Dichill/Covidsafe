"""covidsafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

# Core
from core.views import generateqr
from core.views import generatecode
from core.views import getqrimage
from core.views import home

from accounts.views import RegisterView
from accounts.views import LoginAPI

from knox import views as knox_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # System
    path('api-v1/generate/qr/', generateqr, name="GenQR"),
    path('api-v1/generate/code/', generatecode, name="GenCode"),
    path('api-v1/qrcode/', getqrimage, name="GetImageQr"),

    # Authentication
    path('api-v1/login/', LoginAPI.as_view(), name="login"),
    path('api-v1/register/', RegisterView.as_view(), name="register"),
    path('api-v1/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api-v1/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    # Home
    path('', home, name='home')
]
