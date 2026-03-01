from django.contrib import admin
from .models import Project, ProjectMedia, TechField

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1

@admin.register(TechField)
class TechFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_field', 'created_at')
    list_filter = ('tech_field',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectMediaInline]
