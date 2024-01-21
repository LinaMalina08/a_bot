from django.contrib import admin

from app.internal.models import user

admin.site.register(user.User)
