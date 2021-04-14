from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView,\
    DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('detail/edit/<int:pk>', UpdatePostView.as_view(), name = 'edit_post'),
    path('detail/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('category-list', CategoryListView, name= 'category-list'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]