from django.urls import path
from .views import Store


urlpatterns = [
    path('', Store.as_view()),
    path('category/<int:category_id>/', Store.as_view()),
]

