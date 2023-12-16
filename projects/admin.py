from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'ratings', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Project, ProjectAdmin)
