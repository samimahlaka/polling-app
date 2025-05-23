from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Choice
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.paginator import Paginator
from .serializers import PollSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

#html view for a poll
def poll_detail(request, poll_id):
    poll= get_object_or_404(Poll, id  = poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})


#api view for a poll
@api_view(['GET'])
def get_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return Response(PollSerializer(poll).data)


#html view for vote submit
def vote_submit(request):
    if request.method == "POST":
        choice_id = request.POST.get("choice_id")
        choice = get_object_or_404(Choice, id=choice_id)
        choice.vote +=1
        choice.save()
        #return render(request, 'polls/poll_detail.html', {'poll' : choice.poll} ) ---> template expects a poll 
        return redirect('poll_detail', poll_id = choice.poll.id) #url expects <int:poll_id> i.e poll.id

#api view for vote submit

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def vote_submit_api(request, choice_id):
   choice = get_object_or_404(Choice, id = choice_id)
   choice.vote +=1 
   choice.save()
   return Response({'message': 'Vote added' , 'vote' : choice.vote})


   
@api_view(['GET'])
def poll_result(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return Response(PollSerializer(poll).data)


def polls(request):
    return render(request , 'polls/polls.html')

@api_view(['GET'])
def poll_list(request):
    poll = Poll.objects.all()
    return Response(PollSerializer(poll, many=True).data)

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
    
    
def thankyou(request):
    message = 'Thankyou for voting'
    return render(request, 'polls/thankyou.html', {'message' : message})

@api_view(['GET'])
def api_thankyou(request):
    return Response({'message' : 'Thankyou for voting'})    
    
   
@api_view(['POST'])
def create_poll_with_choices(request):
    question=request.data.get('question')
    choices = request.data.get('choices')
    user_id = request.data.get('user_id')
    
    
    if not user_id or not choices or not question:
        return Response({'error' : 'Question, choices, and user_id are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(id= user_id)
    except User.DoesNotExist:
        return Response({'error': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    poll = Poll.objects.create(question=question,created_by= user)
    
    for choice_text in choices:
         Choice.objects.create(poll=poll , text = choice_text)
    
    return Response({'message': 'Poll created successfully'} , status=status.HTTP_200_OK)

@api_view(['POST'])
def add_choice(request, poll_id):
    try:
        poll = Poll.objects.get(id = poll_id)
        
    except Poll.DoesNotExist:
        return Response({'message' : 'No such poll exist'} , status = status.HTTP_400_BAD_REQUEST)
        
    new_choices= request.data.get('choices')
    
    try:
        for choice_text in new_choices:
            Choice.objects.create(poll=poll, text=choice_text)
            return Response({'message' : 'choices added successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
            
            
@api_view(['GET'])
def api_poll_detail(request, poll_id):
    try:
        poll = Poll.objects.get(id= poll_id)
    except Poll.DoesNotExist:
        return Response({'message': 'No such poll exist'}, status= status.HTTP_400_BAD_REQUEST)
    
    return Response(PollSerializer(poll).data, status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])  
@api_view(['DELETE'])
def api_poll_delete(request, poll_id):
    try:
        poll = Poll.objects.get(id = poll_id)
       
        
    except Poll.DoesNotExist:
        return Response({'message' : 'No such poll exist'} , status = status.HTTP_400_BAD_REQUEST)
    
    if poll.created_by != request.user:
        poll.delete()
        return Response({'message' : 'poll deleted!'} , status = status.HTTP_200_OK)
    else:
        return Response({'message' : 'Authentication not allowed'} , status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_poll_update(request, poll_id):
    try:
        poll = Poll.objects.get(id = poll_id)
    
    except Poll.DoesNotExist:
        return Response({'message' : 'No such poll exist'} , status = status.HTTP_400_BAD_REQUEST)
    
    if request.user != poll.created_by:
        return Response({'message' : 'Authentication not allowed'} , status = status.HTTP_400_BAD_REQUEST)
        
    new_question = request.data.get('question')
    
    if new_question:
        poll.question = new_question
        poll.save()
    
    new_choices = request.data.get('choices')
    
    if new_choices:
        for choice in new_choices:
            Choice.objects.create(poll=poll, text = choice)
        return Response({'message' : 'poll updsted successfully'}, status = 200)
    
    return Response({'message': 'Poll updated successfully'}, status=200)








 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

    
    
        

    