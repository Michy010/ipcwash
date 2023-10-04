from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from . import views

# App level urls configurations
app_name = 'blog'
urlpatterns = [
    path('', views.home , name= 'home'),
    path('about/', views.about , name= 'about'),
    path('leaders/', views.leaders, name= 'leaders'),
    path('post/', views.post , name= 'post'),
    path('create_post/', user_passes_test(views.is_superuser)(views.create_post), name= 'create_post'),
    path('create_leader/', user_passes_test(views.is_superuser)(views.create_leader), name= 'create_leader'),
]