from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.forms import SetPasswordForm
from accounts import views
from.forms import *
# from django.utils.translation import gettext_lazy as _
# from project.forms import MyPasswordChangeForm, MyPasswordResetForm

urlpatterns = [
    # sign in sign up
    path('admin/', admin.site.urls, name='admin'),
    path('sign_up/', views.sign_up, name='sign-up'),
    path('agent_signup/', views.AgentCreationView.as_view(), name='agent_signup'),
    path('client_signup/', views.ClientCreationView.as_view(), name='client_signup'),
    path('sign_in/', views.sign_in, name='sign-in'),
    path('logout/', auth_views.LogoutView.as_view(next_page='sign-in'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html', form_class=MyPasswordChangeForm, success_url='/accounts/passwordchangedone/'),
         name='passwordchange'),
    path('password-change-done/', auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html',),
         name='passwordchangdone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
         template_name='password_resetdone.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name='password_resetconfirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
         template_name='password_reset_complete.html'), name='password_reset_complete'),
]
