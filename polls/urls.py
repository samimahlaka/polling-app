
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:poll_id>/' , views.poll_detail, name = 'poll_detail'),
    path('api/<int:poll_id>/', views.get_poll),
    path('vote/', views.vote_submit, name='vote_submit'),
    path('api/vote/<int:choice_id>/', views.vote_submit_api, name='vote_submit_api'),
    path('results/<int:poll_id>/', views.poll_result),
    path('polls/', views.polls),
    path('api/poll_list/', views.poll_list, name = 'poll_list_api'),
    path('poll_list/',views.poll_list_template, name = 'poll_list'),
    path('api/thankyou/', views.api_thankyou),
    path('thankyou/', views.thankyou),
    path('api/create-poll/', views.create_poll_with_choices, name='create_poll'),
    path('api/add_choices/<int:poll_id>/', views.add_choice),
    path('api/poll_detail/<int:poll_id>/',views.api_poll_detail),
    path('api/poll_delete/<int:poll_id>/', views.api_poll_delete),
    path('api/poll_update/<int:poll_id>/', views.api_poll_update),
    ]