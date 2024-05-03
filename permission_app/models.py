from django.db import models

# Create your models here.
from django.db import models

# from chat_site.settings import AUTH_USER_MODEL
# from user_auth.models import AUTH_USER_MODEL
# from user_auth.models import User
# from user_auth.models import User
# from user_auth.models import User

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    permissions = models.ManyToManyField('Permission', related_name='role_permissions')


class Permission(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField(max_length=50)


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_created_by', null=True,
#                                    blank=True)
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_updated_by', null=True,
#                                    blank=True)