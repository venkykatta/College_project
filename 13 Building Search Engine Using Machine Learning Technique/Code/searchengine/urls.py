"""searchengine URL Configuration

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
from django.urls import path
from django.conf import settings
from user import views as user
from django.conf.urls.static import static
from manager import views as manager
from searchengine import view as search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.index, name='index'),



    path('userlogin/',user.userlogin,name='userlogin'),
    path('userregister/',user.userregister,name='userregister'),
    path('userlogincheck/',user.userlogincheck,name='userlogincheck'),
    path('pagerank',user.pagerank,name='pagerank'),
    path('search/',user.search, name="search"),
    path('search1/',user.search1, name="search1"),
    path('usersearchresult/',user.usersearchresult, name="usersearchresult"),
    path('usersearchresult1/',user.usersearchresult1, name="usersearchresult1"),
    path('weight/', user.weight, name="weight"),
    path('logout/',user.logout,name='logout'),



    path('managerlogin/',manager.managerlogin,name='managerlogin'),
    path('managerregister/',manager.managerregister,name='managerregister'),
    path('managerlogincheck/',manager.managerlogincheck,name='managerlogincheck'),
    path('fileupload/', manager.fileupload, name='fileupload'),




    path('admin1/',search.adminlogin,name='admin1'),
    path('adminloginentered/',search.adminloginentered,name='adminloginentered'),
    path('userdetails/',search.userdetails,name='userdetails'),
    path('Managerdetails/',search.managerdetails,name='Managerdetails'),
    path('activateuser/',search.activateuser,name='activateuser'),
    path('activatemanager/',search.activatemanager,name='activatemanager'),
    path('svm/', search.svm, name="svm"),
    path('xgboost/', search.xgboost, name="xgboost"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
