import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        ''' Nos devuelve True si la fecha de publicación es mayor o igual
            al momento actual menos 1 día, en otras palabras si se publicó 
            desde ayer hacia el futuro ''' 
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default="")
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text