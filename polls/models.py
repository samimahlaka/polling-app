from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=220)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE)
    creted_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.question
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE,  related_name='choices')
    text = models.TextField(max_length=220)
    vote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text
    