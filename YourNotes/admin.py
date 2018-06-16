from django.contrib import admin
from YourNotes.models import User, userNotes
# Register your models here.
admin.site.register(User)
admin.site.register(userNotes)