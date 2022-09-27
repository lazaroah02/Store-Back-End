from django.urls import path
from .views import Store, Categories


urlpatterns = [
    path('', Store.as_view()),
    path('category/<int:category_id>/', Store.as_view()),
    path('product/<int:id_product>/', Store.as_view()),
    path('categories/', Categories.as_view())
]

