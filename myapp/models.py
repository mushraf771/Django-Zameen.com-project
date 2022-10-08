from django.db import models
from django.conf import settings
# from account.models import User
User = settings.AUTH_USER_MODEL
PROPERTY_CATEGORIE = [
    ('BUY', 'BUY'),
    ('RENT', 'RENT'),
    ('Projects', 'Projects')]
PROPERTY_TYPE = [
    ('Homes', 'Homes'),
    ('Plots', 'Plots'),
    ('Commercial', 'Commercial')]
ARIA_UNIT = [('Square Feet', 'Square feet'),
             ('Square meter', 'Square meter'),
             ('Square Yards', 'Square Yards'),
             ('Marla', 'Marla'),
             ('Kanal', 'Kanal')]
OCCUPATION_STATUS = [('Vacant', 'Vacant'), ('Occoupied', 'Occoupied')]
LISTINING_EXPIRY = [('1 Month', '1 Month'), ('3 Month',
                                             '3 Month'), ('6 Month', '6 Month')]

class Property(models.Model):
    agent_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    property_purpose = models.CharField(
        choices=PROPERTY_CATEGORIE, max_length=30,)
    property_types = models.CharField(choices=PROPERTY_TYPE, max_length=30,)
    aria_unit = models.CharField(choices=ARIA_UNIT, max_length=30, )
    aria_size = models.CharField(max_length=30)
    city = models.CharField(max_length=200,)
    price = models.CharField(max_length=255)
    instalment = models.BooleanField(default=False )
    listining_expiry = models.CharField(
        choices=LISTINING_EXPIRY, max_length=30,)
    property_name = models.CharField(max_length=255, )
    property_description = models.CharField(max_length=900, )
    property_type_img = models.ImageField(
        upload_to="uploads/property_type/%y", )
    property_docunments = models.FileField(
        upload_to="uploads/property_docunments/%y", )

    def __str__(self):
        return self.property_purpose + " " + self.property_name


class Property_img(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    property_image = models.ImageField(upload_to="uploads/propety/%y")


APPOINMENT_STATUS = [('Approved', 'Approved'), ('pending', 'pending')]
# def checkagent(request):
#     if request.user == is_agent and is_active:
#         return True
class Appointment(models.Model):
    agent = models.ForeignKey(
        User, on_delete=models.CASCADE)
    appointment_description = models.TextField()
    appointment_date = models.DateTimeField(auto_now_add=True)
    # appoinment_status = models.CharField(
    #     choices=APPOINMENT_STATUS, max_length=30,default='Pending')


class Comment(models.Model):
    user_id = models.ForeignKey(
    User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,)
    phone = models.CharField(max_length=255,)
    description = models.TextField()

    def __str__(self):
        return self.admin_id + " " + self.name

class Notification(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.admin_id + " " + self.name
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    details = models.TextField(max_length=500)
    def __str__(self):
        return self.name + "  " + self.email