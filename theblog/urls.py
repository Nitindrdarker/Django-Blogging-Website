from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove/', views.DeletePostView.as_view(), name='delete_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='Category-list'),
    path('like/<int:pk>/', views.LikePost, name='like_post'),
    path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    
]