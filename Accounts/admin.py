from django.contrib import admin

# Register your models here.
from Accounts.models import User

admin.site.register(User)
