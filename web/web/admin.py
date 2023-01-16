from django.contrib import admin
from web.models import Bug, User

admin.site.register(User)
admin.site.register(Bug)