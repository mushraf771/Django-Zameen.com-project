from .models import User ,Agent ,Client
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
# forms
class AgentCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200,required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'phone', 'address', 'image')
    @transaction.atomic    
    def save(self):
        user = super().save(commit=False)
        user.email =self.cleaned_data.get('email')
        user.is_agent= True
        user.is_staff= True
        user.save()
        agent = Agent.objects.create(user=user)
        return user

    def __init__(self, *args, **kwargs):
        super(AgentCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
class ClientCreationForm(UserCreationForm):
    # email = forms.EmailField(max_length=200,required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1', 'password2','phone','address','image')
    @transaction.atomic    
    def save(self):
        user = super().save(commit=False)
        user.email =self.cleaned_data.get('email')
        user.phone =self.cleaned_data.get('phone')
        user.address =self.cleaned_data.get('address')
        user.is_client= True
        user.save()
        client = Client.objects.create(user=user)
        return user

    def __init__(self, *args, **kwargs):
        super(ClientCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

# password 
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, }))
    new_password1 = forms.CharField(label=_("New Password"),widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),
                                    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    def __init__(self, *args, **kwargs):
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

# reset password
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(
        attrs={'autocomplete': 'email'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'),widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    new_password2 = forms.CharField(label=_('confirm New Password'),widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    def __init__(self, *args, **kwargs):
        super(MySetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname in [ 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None
