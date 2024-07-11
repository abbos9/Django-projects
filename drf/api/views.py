from django.shortcuts import get_object_or_404
from api.models import Author, BookModel, Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status, viewsets
from api.serializer import BookSerializer, AuthorSerializer, RatingSerializer
from django.db.models import Avg
# Create your views here.

# @api_view(["GET", "POST"])
# def get_data(request):
#     if request.method == "GET":
#         books = BookModel.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(f"Created {request.data}", status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class get_data(ListCreateAPIView):
# #     queryset = BookModel.objects.all()
# #     serializer_class = BookSerializer

# @api_view(["GET", "POST"],)
# def get_author(request):
#     if request.method == "POST":
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("Created", status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=400)
#     elif request.method == "GET":
#         author =  Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

# @api_view(['GET', "PUT", "DELETE", "PATCH"])
# def book_detail(request, pk):
#     try:
#         book = BookModel.objects.get(pk=pk)
#     except BookModel.DoesNotExist:
#         return Response({"message": "not found !"})
#     if request.method == "GET":
#         serializer = BookSerializer (book, many=False)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = BookSerializer (instance=book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         book.delete()
#         content = {
#             "message": "Deleted Successfully !"
#         }
#         return Response(data=content, status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PATCH": 
#         serializer = BookSerializer (instance=book, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.data)

# class get_rating(RetrieveUpdateDestroyAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer

# class rating(ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serialized_data = self.get_serializer(queryset, many=True).data

#         # Add average rating to each movie in the response
#         for movie_data in serialized_data:
#             movie = BookModel.objects.get(id=movie_data['id'])
#             movie_data['average_rating'] = movie.ratings.aggregate(Avg('rating'))['rating__avg']

class BookListAPIView(APIView):
    def get(self, request):
        books = BookModel.objects.filter(is_active=True)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Created {request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_book(pk):
    try:
        book = BookModel.objects.get(pk=pk)
    except BookModel.DoesNotExist:
        return Response({"message": "not found !"})
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

class DetailApiView(APIView):
    def get(request, self):
        book = get_object_or_404(BookModel, pk=self.kwargs.get("pk"))
        serializer = BookSerializer(BookModel, many=False)
        if not book:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        book = get_book(pk=pk)
        if not book:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Updated {request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = get_book(pk=pk)
        if not book:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Updated {request.data}", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_book(pk=pk)
        if not book:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        content = {
            "message": "Deleted Successfully!"
        }
        return Response(data=content, status=status.HTTP_204_NO_CONTENT)
