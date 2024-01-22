from django.contrib import admin
from django.urls import path, include
from main.views import CreateView, DeckView, DecksView, EditView, CardView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('decks', DecksView),
    path('deck/<int:index>', DeckView),
    path('card', CardView),
    path('edit/<int:index>', EditView),
    path('create', CreateView),
    path('csrf', views.csrf),
    path('ping', views.ping),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/google/login/', views.GoogleLogin.as_view(), name='google_login'),
]
