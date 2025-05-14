
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:poll_id>/' , views.poll_detail, name = 'poll_detail'),
    path('api/<int:poll_id>/', views.get_poll),
    path('vote/<int:choice_id>/', views.vote_submit),
    path('results/<int:poll_id>/', views.poll_result),
    path('poll_list/', views.poll_list),
]

