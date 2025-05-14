
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:poll_id>/' , views.poll_detail, name = 'poll_detail'),
]
