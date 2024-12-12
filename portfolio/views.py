from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Skill, Experience, Education, Project, Service, Testimonial, BlogPost, Tag, Comment
from markdown import markdown


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


def blogs(request):
    user = User.objects.first()
    blogs = BlogPost.objects.all()

    context = {
        'user': user,
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)


def single_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    user = User.objects.first()
    comments = blog.comments.all()

    # Agar POST so'rovi bo'lsa, yangi sharh qo'shish
    if request.method == "POST":
        user = request.POST['user']
        email = request.POST['email']
        content = request.POST['content']  # Markdown formatida sharh

        # Yangi sharh yaratish
        Comment.objects.create(blog_post=blog, user=user, email=email, content=content)

        # Sharhlar sonini yangilash
        blog.comments_count = blog.comments.count()
        blog.save()

        # Yangi sharh qo'shilgandan so'ng, yana shu blog postiga qaytish
        return redirect('single_blog', blog_id=blog.id)

    # Kontekstga blog va sharhlarni qo'shish
    context = {
        'user': user,
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'single-blog.html', context)



