from django.urls import path
from api.views import BookListAPIView, BookDetail
app_name = "api"

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name="books"),
    # path('authors/', get_author, name="author"),
    path('books/<int:pk>/', BookDetail.as_view(), name="book_detail"),
    # path('rating/<int:pk>/', get_rating.as_view(), name='rating'),
    # path('rating/', rating.as_view(), name="crt_rating" )
]