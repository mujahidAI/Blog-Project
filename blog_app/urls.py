
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from blog_app import views

urlpatterns = [
    # path(' ',admin.site.urls),
    # # path('', views.home,name="home"),
    path('', views.tweet_list,name="tweet_list"),
    path('create/', views.tweet_create, name="tweet_create"),
    path('<int:tweet_id>/edit/', views.tweet_edit,name="tweet_edit"),
    path('<int:tweet_id>/delete/', views.tweet_delete,name="tweet_delete"),
    path('register/', views.register,name="register"),
    path('search/', views.search_view, name="search"),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]



