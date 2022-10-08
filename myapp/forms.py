from django import forms
from django.db import transaction
from .models import Property,Property_img,Appointment,Comment,Contact
from django.utils.translation import gettext , gettext_lazy as _
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('property_purpose', 'property_types',
                'aria_unit', 'aria_size', 'price', 'instalment',
                'listining_expiry', 'property_name', 'property_description',
                'property_type_img', 'property_docunments')
        
# Contact Form
    
class ContactForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), required=True, widget=forms.TextInput(
        attrs={'autocomplete': 'name', 'autofocus': 'name'}))
    email = forms.EmailField(label=_('Email'), required=True,
                             widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    phone = forms.CharField(
        label=_('Phone'), required=True, widget=forms.NumberInput())
    details = forms.CharField(label= _('Message'),required= True,widget= forms.Textarea())
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone','details']
        
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['appointment_status']