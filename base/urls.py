from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Frontend start here!!!
    path('', views.homePage, name = "home"),
    # Frontend end here!!!
    
    
    # Backend start here!!!
    path('dashboard/', views.indexPage, name="index"),
    
    # TypeWritter
    path('typewritter/', views.typewitterPage, name="typewritter"),
    path('typewritter/<slug:slug>/edit', views.typewritterEdit, name="typewritter-edit"),
    path('typewritter/<slug:slug>/delete', views.typewritterDelete, name="typewritter-delete"),
    
    # Fact
    path('fact/', views.factPage, name = "fact"),
    path('fact/<str:pk>/delete/', views.factDelete, name="fact-delete"),
    
    # About
    path('about/', views.aboutPage, name="about"),
    path('about/<str:pk>/delete/', views.aboutDelete, name="about-delete"),
    
    
    # Skill
    path('skill/', views.skillPage, name="skill"),
    path('skill/<slug:slug>/edit', views.skillEdit, name="skill-edit"),
    path('skill/<slug:slug>/delete', views.skillDelete, name="skill-delete"),
    
    # Gallery
    path('gallery/', views.galleryPage, name="gallery"),
    path('gallery/<slug:slug>/edit', views.galleryEdit, name="gallery-edit"),
    path('gallery/<slug:slug>/delete', views.galleryDelete, name="gallery-delete"),
    path('gallery/<slug:slug>/view', views.galleryView, name="gallery-view"),
    
    # MyBlog
    path('myblog/', views.myblogPage, name="myblog"),
    path('myblog/create/', views.myblogCreate, name="myblog-create"),
    path('myblog/<slug:slug>/edit/', views.myblogEdit, name="myblog-edit"),
    path('myblog/<slug:slug>/delete/', views.myblogDelete, name="myblog-delete"),
    path('myblog/<slug:slug>/view/', views.myblogView, name="myblog-view"),
    path('myblog/<slug:slug>/detail/', views.myblogDetail, name="myblog-detail"),
    
    # Contact
    path('contact/', views.contactPage, name="contact"),
    path('contact/<str:pk>/view/', views.contactView, name="contact-view"),
    path('contact/<str:pk>/delete/', views.contactDelete, name="contact-delete"),

    # Search
    path('search/', views.search, name='search')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)