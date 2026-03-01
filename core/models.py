from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class TechField(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    icon_html = models.CharField(max_length=200, blank=True, null=True, help_text="FontAwesome icon class, e.g. 'fa-solid fa-server'")
    resume_pdf = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    cover_image = models.ImageField(upload_to='projects/', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True)
    kaggle_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    time_spent = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., '2 weeks', '3 months'")
    file_size = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., '150 MB', '2.5 GB'")
    tech_field = models.ForeignKey(TechField, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/media/', null=True, blank=True)
    video = models.FileField(upload_to='projects/videos/', null=True, blank=True)
    
    def __str__(self):
        return f"Media for {self.project.title}"
