from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll


def poll_detail(request, poll_id):
    poll= get_object_or_404(Poll, id  = poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})
# Create your views here.
