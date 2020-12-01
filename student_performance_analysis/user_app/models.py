from django.db import models

class QuestionBank(models.Model):
    q_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    opA=models.CharField(max_length=100)
    opB=models.CharField(max_length=100)
    opC=models.CharField(max_length=100)
    opD=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return str(self.q_id)
