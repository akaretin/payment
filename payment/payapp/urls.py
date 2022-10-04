from django.urls import path

from .views import index, buy, item

urlpatterns = [path('', index, name='index'),
               path('buy/<str:id>', buy, name='buy'),
               path('item/<str:id>', item, name='item'),
               ]
