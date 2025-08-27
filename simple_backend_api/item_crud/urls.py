from django.urls import path
from .views import * 

urlspatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]