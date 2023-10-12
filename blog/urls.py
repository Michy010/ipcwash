from django.urls import path
from . import views

# App level urls configurations
app_name = 'blog'
urlpatterns = [
    path('', views.index , name= 'home'),
    path('about/', views.about , name= 'about'),
    path('leaders/', views.leaders, name= 'leaders'),
    path('post/', views.post , name= 'post'),
    path('create_post/', views.create_post, name= 'create_post'),
    path('create_leader/',views.create_leader, name= 'create_leader'),
    path('login/', views.login_page, name= 'login'),
    # path('logout/', views.logout_page, name= 'logout'),
]