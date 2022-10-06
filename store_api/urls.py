from django.urls import path
from .views import Store, GetCategories, VideoView, SearchAnProductView


urlpatterns = [
    path('', Store.as_view()),
    path('category/<int:category_id>/', Store.as_view()),
    path('product/<int:id_product>/', Store.as_view()),
    path('page/<int:page>/', Store.as_view()),
    path('product/<str:name_product>/', SearchAnProductView.as_view()),
    path('categories/', GetCategories.as_view()),
    path('video/', VideoView.as_view())
]

