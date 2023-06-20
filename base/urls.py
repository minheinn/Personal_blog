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
    
     # About
    path('about/', views.aboutPage, name="about"),
    path('about/<str:pk>/delete/', views.aboutDelete, name="about-delete"),
    
    # TypeWritter
    path('typewritter/', views.typewitterPage, name="typewritter"),
    path('typewritter/<str:pk>/edit', views.typewritterEdit, name="typewritter-edit"),
    path('typewritter/<str:pk>/delete', views.typewritterDelete, name="typewritter-delete"),
    
    # Skill
    path('skill/', views.skillPage, name="skill"),
    path('skill/<str:pk>/edit', views.skillEdit, name="skill-edit"),
    path('skill/<str:pk>/delete', views.skillDelete, name="skill-delete"),
    
    # MyBlog
    path('myblog/', views.myblogPage, name="myblog"),
    path('myblog/create/', views.myblogCreate, name="myblog-create"),
    path('myblog/<str:pk>/edit/', views.myblogEdit, name="myblog-edit"),
    path('myblog/<str:pk>/delete/', views.myblogDelete, name="myblog-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)