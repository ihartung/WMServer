"""WMServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from main.views import CreateView, DeckView, DecksView, EditView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('decks', DecksView),
    path('deck/<int:index>', DeckView),
    path('edit/<int:index>', EditView),
    path('create', CreateView),
    path('csrf', views.csrf),
    path('ping', views.ping),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/google/login/', views.GoogleLogin.as_view(), name='google_login'),
]
