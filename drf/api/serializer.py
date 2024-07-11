from django.utils.timezone import now
from rest_framework import serializers
from api.models import BookModel, Author, Rating

class BookSerializer(serializers.ModelSerializer):
    len_of_title = serializers.SerializerMethodField()
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = BookModel
        fields = '__all__'
        
    def validate(self, data):
        if data.get('title') == data.get('description'):
            raise serializers.ValidationError("Title and description cannot be the same")
        return data
    def get_len_of_title(self, object):
        return len(object.title)
    
    def get_days_since_joined(self, obj):
        return (now() - obj.created_at).days


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"