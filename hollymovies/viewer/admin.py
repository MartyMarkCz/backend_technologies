from django.contrib import admin
from django.contrib.auth.models import User
from viewer.models import *


# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)