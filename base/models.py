from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# TyperWritter Page
class TypeWritter(models.Model):
    text = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.text
    
# Facts 
class Fact(models.Model):
    fact_description = RichTextField(null=True, blank=True)
    happy_client = models.IntegerField(null=True)
    project = models.IntegerField(null=True)
    cup_of_coffee = models.IntegerField(null=True)
    award = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def save(self):
        # count will have all of the objects from the Aboutus model
        count = Fact.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = Fact.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 2:
            super(Fact, self).save()
        elif save_permission:
            super(Fact, self).save()

    def has_add_permission(self):
        return Fact.objects.filter(id=self.id).exists()

    
# About Page
class About(models.Model):
    name = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)
    description = RichTextField(null=True, blank=True)
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
    

class Skill(models.Model):
    name = models.CharField(max_length=50, null=True)
    skill = models.IntegerField(null=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __int__(self):
       return self.name

    class Meta:
        unique_together = ('name', 'slug')
   
# Subjects 
SUBJECT = (
   ('A','App'),
   ('W','Web'),
   ('C','Card'),
)

# Gallery
class Gallery(models.Model):
    subject = models.CharField(max_length=3, choices=SUBJECT, null=True)
    slug = AutoSlugField(populate_from='image', unique=True, null=True)
    image = models.ImageField(upload_to="photoes/", null=True)
    
    def __str__(self):
        return str('image')

    class Meta:
        unique_together = ('image', 'slug')
   
   
class MyBlog(models.Model):
    # blog_description =
    title = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    description = RichTextField(null=True)
    blog_image = models.ImageField(upload_to="myblog_image/", null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created', '-updated']

        unique_together = ('title', 'slug')


        
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created', '-updated']
