"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import confirm_email
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('music.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
              name='account_confirm_email'),
    re_path(r'^api/v1/auth/obtain_token/', obtain_jwt_token),
    re_path(r'^api/v1/auth/refresh_token/', refresh_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
