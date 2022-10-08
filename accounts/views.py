from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import AgentCreationForm, ClientCreationForm, MyPasswordChangeForm
from .models import User,Agent,Client
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView

class AgentCreationView(CreateView):
    model = User
    form_class = AgentCreationForm
    template_name ='signup.html'
    def get_context_data(self, **kwargs):
        # kwargs = super().get_context_data(**kwargs)
        kwargs["user_type"] ='agent' 
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        messages.success(request, 'Acount Created Successfully ...!!')
        user = form.save()
        # login(self.request, user)
        return redirect('sign-in')
class ClientCreationView(CreateView):
    model = User
    form_class = ClientCreationForm
    template_name ='signup.html'
    def get_context_data(self, **kwargs):
        # kwargs = super().get_context_data(**kwargs)
        kwargs["user_type"] ='client' 
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('sign-in')
    
# Create your views here.
# login signup


def sign_up(request):
    if request.method == 'POST':
        fm = AgentCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Acount Created Successfully ...!!')
            fm.save()
            print('kaam done ho gayaa he mad saab')
        else:
            messages.info(request, 'Acount Not Created ...!!')
    else:
        fm = AgentCreationForm()
    return render(request, 'signup.html',{'form':fm})


def sign_in(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        print('line 26')
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            print('line 30')
            user = authenticate(username=uname, password=upass)
            print('line 33 he authenticate k baad')
            if user is not None:
                login(request, user)
                print('this is ', user)
                if user.is_active and user.is_superuser:
                    messages.success(request, 'Admin login successfully')
                    return HttpResponseRedirect('/admin')
                else:
                    messages.success(request, 'login successfully')
                    return HttpResponseRedirect('/index/')
        
    else:
        fm = AuthenticationForm()
    return render(request, 'signin.html',{'form':fm})


# web passwords
def MyPasswordChange(request):
    if request.method == 'POST':
        fm = MyPasswordChangeForm(request.POST)
        if fm.is_valid():
            print(fm, 'line 165')
            fm.save()
    # fm = MyPasswordChangeForm()
    return render(request, 'passwordchange.html')