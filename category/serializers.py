from .models import Category, SubCategory
from rest_framework import serializers, validators


class CategorySerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=Category.objects.all())], max_length=255)

    def create(self, validated_data):
        category = Category(
            category_name=validated_data['category_name']
        )
        category.save()
        return category

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'createdAt', 'updatedAt')
