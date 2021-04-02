from django.contrib import admin
from .models import Polls, Voted

# Register your models here.
admin.site.register(Polls)
admin.site.register(Voted)