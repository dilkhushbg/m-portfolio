from django.shortcuts import render, get_object_or_404
from .models import Project, TechField

def home(request):
    tech_fields = TechField.objects.all().order_by('created_at')
    return render(request, 'home.html', {'tech_fields': tech_fields})

def projects(request):
    projects_list = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects_list})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def tech_domains(request):
    tech_fields = TechField.objects.all().order_by('created_at')
    return render(request, 'tech_domains.html', {'tech_fields': tech_fields})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
