# admin.py
from django.contrib import admin
from .models import User, Skill, Experience, Education, Project, Service, Testimonial, BlogPost, Tag

# Register each model with the admin site
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(BlogPost)
admin.site.register(Tag)
