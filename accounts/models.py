from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
#NEW , CODE_VERIFY , DONE, PHOTO_DONE
#VIA_PHONE, VIA_EMAIL
#CUSTOMER, SELLER


class CustomUser(BaseModel , AbstractUser):
    user_role = models.CharField()
    auth_type = models.CharField()
    auth_status = models.CharField
    email = models.EmailField(max_length=133 , unique= True , null= True , blank=True)
    phone_number = models.CharField(max_length=13 , null=True , blank=True)
    photo = models.ImageField(upload_to='accounts/',blank=True, null=True)
