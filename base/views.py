from django.shortcuts import render, redirect
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages #import messages
import json
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Frontend start here!!!
def homePage(request):
    text= TypeWritter.objects.values_list("text",flat=True)
    texts = json.dumps(list(text))
    
    abouts = About.objects.all()
    facts = Fact.objects.all()
    skills = Skill.objects.all()
    galleries = Gallery.objects.all()
    blogs = MyBlog.objects.all()[1:4]
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
        )
        return redirect('home')
    context = {'forms':forms}
    
    context = {'texts':texts, 'abouts':abouts, 'facts':facts, 'skills':skills, 'blogs':blogs, 'galleries':galleries}
    return render(request, 'frontend/home.html', context)


# Backend start here!!!
@login_required (login_url='login')
def indexPage(request):
    texts = TypeWritter.objects.all()
    abouts = About.objects.all()
    skills = Skill.objects.all()
    galleries = Gallery.objects.all()
    blogs = MyBlog.objects.all()
    context = {'texts':texts, 'abouts':abouts, 'skills':skills, 'galleries':galleries, 'blogs':blogs}
    return render(request, 'backend/index.html', context)


# TypeWritter Page start here!!!
@login_required (login_url='login')
def typewitterPage(request):
    page = "typerwritter-create"
    abouts = About.objects.all()
    forms = TypeWritterForm()
    texts = TypeWritter.objects.all()
    if request.method == 'POST':
        form = TypeWritterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Add TyperWritter is sucessfully!" )
            return redirect('typewritter')
    context = {'page':page,'forms':forms, 'texts':texts, 'abouts':abouts}
    return render(request, 'backend/typewritter/typewritter.html', context)

@login_required (login_url='login')
def typewritterEdit(request, pk):
    text = TypeWritter.objects.get(id=pk)
    texts = TypeWritter.objects.all()
    forms = TypeWritterForm(instance=text)
    if request.method == "POST":
        form = TypeWritterForm(request.POST, instance=text)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Update Typerwritter is sucessfully!" )
            return redirect('typewritter')
    context = {'text':text, 'forms':forms, 'texts':texts}
    return render(request, 'backend/typewritter/typewritter.html', context)

@login_required (login_url='login')
def typewritterDelete(request,pk):
    text = TypeWritter.objects.get(id=pk)
    if request.method == "POST":
        text.delete()
        messages.success(request, "Your Delete TypeWritter is sucessfully!" )
        return redirect('typewritter')    
    return render(request, 'backend/typewritter/delete.html')
# Typerwritter Page end here!!!

# Facts Page start here!!!
@login_required (login_url='login')
def factPage(request):
    page = "fact-create"
    abouts = About.objects.all()
    facts = Fact.objects.all()
    fact = Fact.objects.first()
    if not fact:
        forms = FactForm()
        if request.method == "POST":
            form = FactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Fact add is sucessfully!')
                return redirect('fact')
        context = {'abouts':abouts, 'forms':forms, 'fact':fact, 'page':page}
        return render(request, 'backend/fact/fact.html', context)
    else:
        fact = Fact.objects.latest('id')
        abouts = About.objects.all()
        forms = FactForm(instance=fact)
        if request.method == "POST":
            form = FactForm(request.POST, instance=fact)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Edit Fact is sucessfully!" )
                return redirect('fact')
        context = {'fact':fact, 'forms':forms,'page':page, 'facts':facts, 'abouts':abouts}
        return render(request, 'backend/fact/fact.html', context)
        
@login_required (login_url='login')
def factDelete(request, pk):
    fact = Fact.objects.latest('id')
    if request.method == "POST":
        fact.delete()
        messages.success(request, "Your Delete About is sucessfully!" )
        return redirect('fact')
    context = {'fact':fact}
    return render(request, 'backend/fact/delete.html', context)
# Facts Page end here!!!

# AboutPage start here!!!!!
@login_required (login_url='login')
def aboutPage(request):
    page = "about-create"
    abouts = About.objects.all()
    about = About.objects.first()
    if not about:
        forms = AboutForm()
        if request.method == "POST":
            form = AboutForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your About add is sucessfully!')
                return redirect('about')
        context = {'forms':forms, 'about':about, 'page':page}
        return render(request, 'backend/about/about.html', context)
    else:
        about = About.objects.latest('id')
        forms = AboutForm(instance=about)
        if request.method == "POST":
            form = AboutForm(request.POST, instance=about)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Edit About is sucessfully!" )
                return redirect('about')
        context = {'about':about, 'about':about, 'forms':forms,'page':page, 'abouts':abouts}
        return render(request, 'backend/about/about.html', context)

@login_required (login_url='login')
def aboutDelete(request, pk):
    about = About.objects.latest('id')
    if request.method == "POST":
        about.delete()
        messages.success(request, "Your Delete About is sucessfully!" )
        return redirect('about')
    context = {'about':about}
    return render(request, 'backend/about/delete.html', context)

# AboutPage end here!!!

# skillPage start here!!!
@login_required (login_url='login')
def skillPage(request):
    abouts = About.objects.all()
    page = "skill-create"
    forms = SkillForm()
    skills = Skill.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your  {} add Skill is sucessfully!".format(name) )
            return redirect('skill')
    context = {'forms':forms, 'skills':skills, 'page':page, 'abouts':abouts}
    return render(request, 'backend/skill/skill.html', context)

@login_required (login_url='login')
def skillEdit(request, slug):
    skill = Skill.objects.get(slug=slug)
    skills = Skill.objects.all()
    forms = SkillForm(instance=skill)
    if request.method == "POST":
        name = request.POST.get('name')
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Edit {} is sucessfully!".format(name) )
            return redirect('skill')
    context = {'skill':skill, 'skills':skills, 'forms':forms}
    return render(request, 'backend/skill/skill.html', context)

@login_required (login_url='login')
def skillDelete(request, slug):
    skill = Skill.objects.get(slug=slug)
    if request.method == "POST":
        name = request.POST.get('name')
        skill.delete()
        messages.success(request, "Your Delete {} is sucessfully!".format(name) )
        return redirect('skill')
    context = {'skill':skill}
    return render(request, 'backend/skill/delete.html', context)
# skillPage end here!!!

# Gallery Page start here!!!
@login_required (login_url='login')
def galleryPage(request):
    abouts = About.objects.all()
    page = "gallery-create"
    forms = GalleryForm()
    galleries = Gallery.objects.all()
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        messages.success(request, "Your Add Gallery is sucessfully!" )
        return redirect('gallery')
    context = {'page':page,'forms':forms, 'galleries':galleries, 'abouts':abouts}
    return render(request, 'backend/gallery/gallery.html', context)

@login_required (login_url='login')
def galleryEdit(request, slug):
    gallery = Gallery.objects.get(slug=slug)
    galleries = Gallery.objects.all()
    forms = GalleryForm(instance=gallery)
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Update Gallery is sucessfully!" )
            return redirect('gallery')
    context ={'gallery':gallery, 'galleries':galleries, 'forms':forms}
    return render(request, 'backend/gallery/gallery.html', context)

@login_required (login_url='login')
def galleryDelete(request, slug):
    gallery = Gallery.objects.get(slug=slug)
    if request.method == "POST":
        gallery.delete()
        messages.success(request, "Your Delete Gallery is sucessfully!")
        return redirect('gallery')
    return render(request, 'backend/gallery/delete.html')

@login_required (login_url='login')
def galleryView(request, slug):
    galleries = Gallery.objects.get(slug=slug)
    context = {'galleries':galleries}
    return render(request, 'backend/gallery/view.html', context)
# Gallery Page end here!!!


#Myblog Page Start here!!!
@login_required (login_url='login')
def myblogPage(request):
    blogs = MyBlog.objects.all()
    abouts = About.objects.all()
    context = {'blogs':blogs, 'abouts':abouts}
    return render(request, 'backend/myblog/myblog.html', context)

@login_required (login_url='login')
def myblogCreate(request):
    forms = MyBlogForm()
    if request.method == "POST":
        form = MyBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Add Blog is sucessfully!" )
            return redirect('myblog')
    context = {'forms':forms}
    return render(request, 'backend/myblog/create.html', context)

@login_required (login_url='login')
def myblogEdit(request, slug):
    blog = MyBlog.objects.get(slug=slug)
    forms = MyBlogForm(instance=blog)
    if request.method == "POST":
        form = MyBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Edit MyBlog is sucessfully!" )
            return redirect('myblog')
    context = {'blog':blog, 'forms':forms}
    return render(request, 'backend/myblog/edit.html', context)

@login_required (login_url='login')
def myblogDelete(request, slug):
    blog = MyBlog.objects.get(slug=slug)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Your Delete MyBlog is sucessfully!" )
        return redirect('myblog')
    context = {'blog':blog}
    return render(request, 'backend/myblog/delete.html', context)

@login_required (login_url='login')
def myblogView(request, slug):
    blogs = MyBlog.objects.get(slug=slug)
    context = {'blogs':blogs}
    return render(request, 'backend/myblog/view.html', context)

@login_required (login_url='login')
def myblogDetail(request,slug):
    new_search = request.GET.get('search') if request.GET.get('search') != None else ''
    blogss = MyBlog.objects.filter(
        Q(title__contains = new_search)
        )
    blogs = MyBlog.objects.all()
    blog = MyBlog.objects.get(slug=slug)
    context ={'blogs':blogs,'blog':blog, 'blogss':blogss}
    return render(request, 'frontend/blogdetail.html', context)
#Myblog Page End here!!!

#Contact Page Start here!!!
@login_required (login_url='login')
def contactPage(request):
    abouts = About.objects.all()
    contacts = Contact.objects.all()
    context = {'abouts':abouts,'contacts':contacts}
    return render(request, 'backend/contact/contact.html', context)

@login_required (login_url='login')
def contactDelete(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        messages.success(request, "Your Delete Contact is sucessfully!" )
        return redirect('contact')
    context = {'contact':contact}
    return render(request, 'backend/contact/delete.html', context)

@login_required (login_url='login')
def contactView(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact':contact}
    return render(request, 'backend/contact/view.html', context)
#Contact Page End here!!!
