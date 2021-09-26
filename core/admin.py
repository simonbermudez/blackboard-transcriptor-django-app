from django.contrib import admin
from .models import *

# Register your models here.
models = [School, Program, Course]

for model in models:
    admin.site.register(model)