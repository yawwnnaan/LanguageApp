from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)

    def __str__(self):
        return self.word

class Test(models.Model):
    question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=50)
    incorrect_answer1 = models.CharField(max_length=50)
    incorrect_answer2 = models.CharField(max_length=50)
    incorrect_answer3 = models.CharField(max_length=50)

    def __str__(self):
        return self.question