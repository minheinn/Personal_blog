from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): # Here
        return not About.objects.exists()
    
class TypeWritterAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
admin.site.register(TypeWritter, TypeWritterAdmin)

# Facts
@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): # Here
        return not Fact.objects.exists()

class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'skill']
admin.site.register(Skill, SkillAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject','image']
admin.site.register(Gallery, GalleryAdmin)

class MyBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'blog_image', 'created', 'updated']
admin.site.register(MyBlog, MyBlogAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'created', 'updated']
admin.site.register(Contact, ContactAdmin)