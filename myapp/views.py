from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from .models import Property
# from .models import Agent
from django.contrib import messages
from .filters import PropertyFilter
# sigup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import PropertyForm
from .models import Contact
from .models import Appointment
# from .forms import AddPropertyForm
from .forms import ContactForm
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


class Plots(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'plots.html')


def MyMapp(request):
    return render(request, 'maps.html')


class AddProperty(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'addproperty.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["user_type"] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
# @login_required(login_url='sign-in')
def AddProperti(request):
    form = PropertyForm()
    if request.method == 'POST':
        fm = PropertyForm(request.POST, request.FILES)
        if fm.is_valid():
            property_purpose = fm.cleaned_data['property_purpose']
            property_types = fm.cleaned_data['property_types']
            aria_unit = fm.cleaned_data['aria_unit']
            aria_size = fm.cleaned_data['aria_size']
            price = fm.cleaned_data['price']
            instalment = fm.cleaned_data['instalment']
            listining_expiry = fm.cleaned_data['listining_expiry']
            property_name = fm.cleaned_data['property_name']
            property_description = fm.cleaned_data['property_description']
            property_type_img = fm.cleaned_data['property_type_img']
            property_docunments = fm.cleaned_data['property_docunments']
            user = request.user
            data = Property(agent_id=user,
                property_purpose=property_purpose,
                property_types=property_types,
                aria_unit=aria_unit,
                aria_size=aria_size,
                price=price,
                instalment=instalment,
                listining_expiry=listining_expiry,
                property_name=property_name,
                property_description=property_description,
                property_type_img=property_type_img,
                property_docunments=property_docunments)
            messages.success(request, 'Acount Created Successfully ...!!')
            data.save()
            print(data, 'ye data he line 96 he')
        else:
            print('data is invalid')
            messages.error(request,'adding failed')
            return render(request, 'addproperty.html',{'form': form})
    else:
        form = PropertyForm()
    return render(request, 'addproperty.html',{'form':form})
    #     return HttpResponseRedirect('/sign_in/')


def Homes(request):
    myfilter = PropertyFilter()
    context = {'form':myfilter}
    return render(request, 'homes.html',context)


def Rent(request):
    return render(request, 'rent.html')


def Contactus(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        user = request.user
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            details = form.cleaned_data.get('details')
            data = Contact( name=name, email=email, phone=phone, details=details)
            messages.success(request, 'Thnks for Contacting  ')
            data.save()
        # else:
            # messages.error(request, 'Submission Failed')
            # form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def Appointments(request):
    form = AppointmentForm()
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            appointment_description = form.cleaned_data['appointment_description']
            data = Appointment(agent=user, appointment_description=appointment_description)
            data.save()
    return render(request, 'appoinments.html',{'form': form})


# dashboard 
@login_required(login_url='sign-in')
def Index(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='sign-in')
def Charts(request):
    return render(request, 'dashboard/charts.html')


@login_required(login_url='sign-in')
def AdminTable(request):
    return render(request, 'dashboard/tables.html')


@login_required(login_url='sign-in')
def SideNav_Light(request):
    return render(request, 'dashboard/sidenav.html')


@login_required(login_url='sign-in')
def Layout_Static(request):
    return render(request, 'dashboard/static.html')


@login_required(login_url='sign-in')
def Password(request):
    return render(request, 'dashboard/password.html')


def Error401(request):
    return render(request, 'dashboard/401.html')


def Error404(request):
    return render(request, 'dashboard/404.html')


def Error500(request):
    return render(request, 'dashboard/500.html')
