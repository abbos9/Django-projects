from django.urls import path

from blogs.views import CommentView,PageBlogDetailtView, add_to_like, PageBLogView

app_name = 'blogs'

urlpatterns = [
    path("<int:pk>/comment/", CommentView, name='comment'),
    path('<int:pk>/blog_detail/', PageBlogDetailtView.as_view(), name='blog_detail'),
    path('<int:product_pk>/like/', add_to_like, name='like'),
    path('blog/', PageBLogView.as_view(), name='blog'),
]