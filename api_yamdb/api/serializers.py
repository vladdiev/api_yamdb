from django.core.validators import MaxValueValidator
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Serializer for getting a list of all titles."""
    caregory = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField(default=0)
    
    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('__all__',)


class TitleViewSerializer(serializers.ModelSerializer):
    """Serializer for working with a title."""
    category = SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    year = serializers.IntegerField(
        validators=[MaxValueValidator(timezone.now().year)],
    )

    class Meta:
        model = Title
        fields = '__all__'
