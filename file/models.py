from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return '%s/%s' % (self.question_text,self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return '%s/%d' % (self.choice_text,self.votes) #이게 더 좋음. 무조건 s로처리하는게 젤 상위임. 
        #return self.choice_text +str(self.votes)
