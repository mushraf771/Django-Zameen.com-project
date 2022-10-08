from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth import views as auth_views
# from project.forms import MyPasswordChangeForm, MyPasswordResetForm

urlpatterns = [
    path('addproperty/', views.AddProperty.as_view(), name='addproperty'),
    path('adproperty/', views.AddProperti, name='adproperty'),
    path('homes/', views.Homes, name='homes'),
    path('contact/', views.Contactus, name='contact'),
    path('rent/', views.Rent, name='rent'),
    path('', views.HomePage.as_view(), name='home'),
    path('base/', views.Base.as_view(), name='base'),
    path('plots/', views.Plots.as_view(), name='plots'),
    path('map/', views.MyMapp, name='mymapp'),
    path('appointment/', views.Appointments, name='appointment'),
    
    # dashboard
    path('index/', views.Index, name='index'),
    path('charts/', views.Charts, name='chart'),
    path('admintable/', views.AdminTable, name='admin-table'),
    path('sidenav_light/', views.SideNav_Light, name='sidenav_light'),
    path('layout_static/', views.Layout_Static, name='layout_static'),
    # path('password/', views.Password, name='password'),
    path('error401/', views.Error401, name='error401'),
    path('error404/', views.Error404, name='error404'),
    path('error500/', views.Error500, name='error500'),
]
