"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('registion/',views.registion,name='registion'),
    path('regis/',views.regis,name='regis'),
    path('logindata/',views.logindata,name='logindata'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('about1/<int:pk>',views.about1,name='about1'),
    path('home/<int:pk>',views.home,name='home'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('dashbord/<int:pk>',views.dashbord,name='dashbord'),
    path('first/<int:pk>',views.first,name='first'),
    path('second/',views.second,name='second'),
    path('third/',views.third,name='third'),
    path('fourth/',views.fourth,name='fourth'),
    path('five/',views.five,name='five'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
