from django.contrib import admin
from .models import About, Skill, Education, Experience, Service, ContactMessage

# About model
admin.site.register(About)

# Skills model
admin.site.register(Skill)

# Education model
admin.site.register(Education)

# Experience model
admin.site.register(Experience)

# Services model
admin.site.register(Service)

# ContactMessage model
admin.site.register(ContactMessage)