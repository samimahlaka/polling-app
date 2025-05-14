from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll
from rest_framework.decorators import api_view
from  rest_framework import status
from .serializers import PollSerializer
from rest_framework.response import Response

def poll_detail(request, poll_id):
    poll= get_object_or_404(Poll, id  = poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})
# Create your views here.

@api_view(['GET'])
def get_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return Response(PollSerializer(poll).data)