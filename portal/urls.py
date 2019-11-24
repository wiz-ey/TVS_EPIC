from django.urls import path
from . import views

urlpatterns = [

    path('about/',views.AboutView.as_view(),name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.CreatePostView.as_view(), name='create_post'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/bid/', views.add_bid_to_post, name='add_bid_to_post'),
    path('post/<int:pk>/deactivate/', views.post_deactivate, name='post_deactivate'),
    path('post/<int:pk>/activate/', views.post_activate, name='post_activate'),
    path('post/<int:pk>/vr/', views.VrView.as_view(), name='vr_view')


]
