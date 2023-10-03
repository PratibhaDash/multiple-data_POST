from django.urls import path
from .views import MyModelListCreateView

urlpatterns = [
    path('mymodels/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
    
]
