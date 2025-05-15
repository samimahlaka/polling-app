from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Choice
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator
from .serializers import PollSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

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

# @api_view(['GET'])
# def poll_list(request):
#     poll = Poll.objects.all()
#     return Response(PollSerializer(poll, many=True).data)

class PollListView(ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
    

def poll_list_html(request):
    page =  request.GET.get('page' , 1);
    response = request.get(f'http://127.0.0.1:8000/polls/poll_list/?page={page}')
    data = response.JSON()
    return render(request,'poll_list.html',{'data' : data})


def poll_list_template(request):
    poll = Poll.objects.all()
    page_number = request.GET.get('page')
    paginator =Paginator(poll, 5)
    page = paginator.get_page(page_number)
    return render(request , 'polls/poll_list_template.html', {'page' : page})
    
    
        