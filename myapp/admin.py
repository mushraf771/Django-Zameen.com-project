from django.contrib import admin
from myapp.models import Property, Contact, Property_img, Appointment, Comment, Notification
# Register your models here.
admin.site.register(Property)
admin.site.register(Property_img)
admin.site.register(Appointment)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Contact)
