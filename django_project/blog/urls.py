from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView



urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)