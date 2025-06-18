from django.contrib import admin
from .models import Project, Skill, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology', 'created_date']
    list_filter = ['technology', 'created_date']
    search_fields = ['title', 'description']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category', 'proficiency']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date']
    list_filter = ['created_date']
    readonly_fields = ['created_date']