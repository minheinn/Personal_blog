from django.shortcuts import render, redirect
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages #import messages
import json
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Frontend start here!!!
def homePage(request):
    text= TypeWritter.objects.values_list("text",flat=True)
    texts = json.dumps(list(text))
    
    abouts = About.objects.all()
    skills = Skill.objects.all()
    blogs = MyBlog.objects.all()[1:4]
    
    context = {'texts':texts, 'abouts':abouts, 'skills':skills, 'blogs':blogs}
    return render(request, 'frontend/home.html', context)



# Backend start here!!!
@login_required (login_url='login')
def indexPage(request):
    abouts = About.objects.all()
    context = {'abouts':abouts}
    return render(request, 'backend/index.html', context)

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
def skillEdit(request, pk):
    skill = Skill.objects.get(id=pk)
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
def skillDelete(request, pk):
    skill = Skill.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        skill.delete()
        messages.success(request, "Your Delete {} is sucessfully!".format(name) )
        return redirect('skill')
    context = {'skill':skill}
    return render(request, 'backend/skill/delete.html', context)
# skillPage end here!!!


#Myblog Page Start here!!!
def myblogPage(request):
    blogs = MyBlog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'backend/myblog/myblog.html', context)

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

def myblogEdit(request, pk):
    blog = MyBlog.objects.get(id=pk)
    forms = MyBlogForm(instance=blog)
    if request.method == "POST":
        form = MyBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Edit MyBlog is sucessfully!" )
            return redirect('myblog')
    context = {'blog':blog, 'forms':forms}
    return render(request, 'backend/myblog/edit.html', context)

def myblogDelete(request, pk):
    blog = MyBlog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Your Delete MyBlog is sucessfully!" )
        return redirect('myblog')
    context = {'blog':blog}
    return render(request, 'backend/myblog/delete.html', context)
#Myblog Page End here!!!