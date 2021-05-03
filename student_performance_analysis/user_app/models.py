from django.db import models

class Aptitude(models.Model):
    q_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    opA=models.CharField(max_length=100)
    opB=models.CharField(max_length=100)
    opC=models.CharField(max_length=100)
    opD=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return "question no : "+str(self.q_id)
class Communication(models.Model):
    q_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    opA=models.CharField(max_length=100)
    opB=models.CharField(max_length=100)
    opC=models.CharField(max_length=100)
    opD=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return "question no : "+str(self.q_id)
class ProgrammingLogic(models.Model):
    q_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    opA=models.CharField(max_length=100)
    opB=models.CharField(max_length=100)
    opC=models.CharField(max_length=100)
    opD=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return "question no : "+str(self.q_id)
class Reasoning(models.Model):
    q_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    opA=models.CharField(max_length=100)
    opB=models.CharField(max_length=100)
    opC=models.CharField(max_length=100)
    opD=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return "question no : "+str(self.q_id)
class Management(models.Model):
    q_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    opA=models.CharField(max_length=100)
    opB=models.CharField(max_length=100)
    opC=models.CharField(max_length=100)
    opD=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return "question no : "+str(self.q_id)
