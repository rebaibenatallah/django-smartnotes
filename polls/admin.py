from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(poll)
admin.site.register(poll_option)
admin.site.register(voters)