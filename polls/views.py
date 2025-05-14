from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Choice
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

@api_view(['POST'])
def vote_submit(request, choice_id):
    choice = get_object_or_404(Choice, id = choice_id)
    choice.vote += 1
    choice.save()
    return Response({'message' : 'Vote added' , 'votes':choice.vote})

@api_view(['GET'])
def poll_result(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return Response(PollSerializer(poll).data)

@api_view(['GET'])
def poll_list(request):
    poll = Poll.objects.all()
    return Response(PollSerializer(poll, many=True).data)
        