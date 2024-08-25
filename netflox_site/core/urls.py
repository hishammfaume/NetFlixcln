from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('login/', views.login_view, name='login'),
   # path('signup', views.signup, name='signup'),
    path('movie/', views.movie, name='movie'),
   path('tvshow/', views.tv_show, name='tvshow'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),



   
]