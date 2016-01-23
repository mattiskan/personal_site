from django.contrib import admin
from blog.models import BlogEntry, EmailSubscribers

admin.site.register(BlogEntry)
admin.site.register(EmailSubscribers)

