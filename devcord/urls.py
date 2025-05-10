from django.contrib import admin
from django.urls import path, include
from chat.views import register
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
