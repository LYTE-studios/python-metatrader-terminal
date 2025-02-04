"""
URL configuration for api project.

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
from django.urls import path, include
from tradely.views import MTAccountAuthView, TradeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/mt-account/', MTAccountAuthView.as_view(), name='mt-auth'),
    path('trades/<int:account_id>/', TradeListView.as_view(), name='trade-list'),
    path('api/', include('tradely.urls')),
    
]
