from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tag/<str:slug>/', views.tags_page)
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index)
]