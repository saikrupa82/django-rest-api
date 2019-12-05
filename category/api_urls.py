from django.urls import path
from category.views import *

urlpatterns = [
    path('list', GetCategoryList.as_view()),
    path('create', CreateCategory.as_view()),
    path('sub-category/create', CreateSubCategory.as_view()),
]
