from django.contrib import admin
from accounts.models import User,Agent,Client,Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Client)
admin.site.register(Profile)
