from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self):
        # count will have all of the objects from the Aboutus model
        count = About.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = About.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 2:
            super(About, self).save()
        elif save_permission:
            super(About, self).save()

    def has_add_permission(self):
        return About.objects.filter(id=self.id).exists()
    
class TypeWritter(models.Model):
    text = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.text
    

class Skill(models.Model):
    name = models.CharField(max_length=50, null=True)
    skill = models.IntegerField(null=True)
    
    def __int__(self):
       return self.name
   
   
class MyBlog(models.Model):
    # blog_description =
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    blog_image = models.ImageField(upload_to="myblog_image/", null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created', '-updated']