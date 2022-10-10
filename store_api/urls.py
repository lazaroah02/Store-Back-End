from django.urls import path
from . import views


urlpatterns = [
    path('', views.Store.as_view()),
    path('category/<int:category_id>/', views.Store.as_view()),
    path('category/<int:category_id>/page/<int:page>/', views.Store.as_view()),
    path('product/<int:id_product>/', views.GetEspecificProduct.as_view()),
    path('page/<int:page>/', views.Store.as_view()),
    path('product/<str:name_product>/', views.SearchAnProductView.as_view()),
    path('categories/', views.GetCategories.as_view()),
    path('video/', views.VideoView.as_view())
]

