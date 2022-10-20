from django.contrib import admin

from app.models import Candidate, Career
from .models import *
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Career)