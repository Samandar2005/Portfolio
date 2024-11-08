from django.shortcuts import render, get_object_or_404
from .models import User, Skill, Experience, Education, Project, Service, Testimonial, BlogPost, Tag


def index(request):
    user = User.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    tags = Tag.objects.all()

    context = {
        'user': user,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'projects': projects,
        'services': services,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'tags': tags,
    }
    return render(request, 'index.html', context)
