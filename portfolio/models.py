from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about = models.TextField()
    contact_email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_projects = models.IntegerField(default=0)
    total_volunteers = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    profile_logo = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(User, related_name="skills", on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    proficiency = models.IntegerField()

    def __str__(self):
        return f"{self.skill_name} - {self.proficiency}%"


class Experience(models.Model):
    user = models.ForeignKey(User, related_name="experiences", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    user = models.ForeignKey(User, related_name="education", on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Service(models.Model):
    user = models.ForeignKey(User, related_name="services", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    i_class_name = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    user = models.ForeignKey(User, related_name="testimonials", on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.client_name}"


class BlogPost(models.Model):
    user = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    views = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name="tags", on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag
