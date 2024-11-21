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


def about(request):
    user = User.objects.first()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'user': user,
        'skills': skills,
        'testimonials': testimonials,
    }

    return render(request, 'about-us.html', context)


def services(request):
    user = User.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'user': user,
        'skills': skills,
        'services': services,
        'testimonials': testimonials,
    }

    return render(request, 'services.html', context)


def portfolio(request):
    projects = Project.objects.all()
    user = User.objects.first()

    context = {
        'projects': projects,
        'user': user,
    }

    return render(request, 'portfolio.html', context)


def contact_us(request):
    user = User.objects.first()

    context = {
        'user': user,
    }

    return render(request, 'contact.html', context)


def blog(request):
    user = User.objects.first()

    context = {
        'user': user,
    }

    return render(request, 'blog.html', context)