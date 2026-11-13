from django.contrib import admin

from tellthem.models import Entry, Topic

# Register your models here.
admin.site.register(Topic)  # Replace 'YourModelName' with the actual model you want to register
admin.site.register(Entry)  # Register the Entry model as well