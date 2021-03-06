from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'), 
    path('edit/<int:pk>/', views.UpdateStoryView.as_view(), name='updateStory'),
    path('delete/<int:pk>/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('author/<int:pk>/', views.AuthorsListView.as_view(), name= 'author'),
    path('category/<str:cats>/', views.CategoryListView.as_view(), name='category'),
]
