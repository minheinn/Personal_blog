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
    path('typewritter/<str:pk>/edit', views.typewritterEdit, name="typewritter-edit"),
    path('typewritter/<str:pk>/delete', views.typewritterDelete, name="typewritter-delete"),
    
    # Fact
    path('fact/', views.factPage, name = "fact"),
    path('fact/<str:pk>/delete/', views.factDelete, name="fact-delete"),
    
    # About
    path('about/', views.aboutPage, name="about"),
    path('about/<str:pk>/delete/', views.aboutDelete, name="about-delete"),
    
    
    # Skill
    path('skill/', views.skillPage, name="skill"),
    path('skill/<str:pk>/edit', views.skillEdit, name="skill-edit"),
    path('skill/<str:pk>/delete', views.skillDelete, name="skill-delete"),
    
    # Gallery
    path('gallery/', views.galleryPage, name="gallery"),
    path('gallery/<str:pk>/edit', views.galleryEdit, name="gallery-edit"),
    path('gallery/<str:pk>/delete', views.galleryDelete, name="gallery-delete"),
    path('gallery/<str:pk>/view', views.galleryView, name="gallery-view"),
    
    # MyBlog
    path('myblog/', views.myblogPage, name="myblog"),
    path('myblog/create/', views.myblogCreate, name="myblog-create"),
    path('myblog/<str:pk>/edit/', views.myblogEdit, name="myblog-edit"),
    path('myblog/<str:pk>/delete/', views.myblogDelete, name="myblog-delete"),
    path('myblog/<str:pk>/view/', views.myblogView, name="myblog-view"),
    path('myblog/<str:pk>/detail/', views.myblogDetail, name="myblog-detail"),
    
    # Contact
    path('contact/', views.contactPage, name="contact"),
    path('contact/<str:pk>/view/', views.contactView, name="contact-view"),
    path('contact/<str:pk>/delete/', views.contactDelete, name="contact-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)