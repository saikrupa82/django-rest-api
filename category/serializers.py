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


class SubCategorySerializers(serializers.ModelSerializer):
    sub_category_name = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=SubCategory.objects.all())], max_length=255)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        instance = SubCategory(
            sub_category_name=validated_data['sub_category_name'],
            category_id=validated_data['category_id']
        )
        instance.save()
        return instance

    class Meta:
        model = SubCategory
        fields = ('id', 'category_id', 'sub_category_name', 'createdAt', 'updatedAt')
