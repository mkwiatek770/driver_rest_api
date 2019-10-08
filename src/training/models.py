from django.db import models


class Training(models.Model):
    advice = models.OneToOneField('advice.Advice', on_delete=models.CASCADE)

    def __str__(self):
        return "Training for {}".format(self.advice.title)


class Question(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    question = models.TextField()
    answers = models.ManyToManyField('training.Answer')

    def __str__(self):
        return "{}...".format(self.question[:30])


class Answer(models.Model):
    anwer = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return "{}...".format(self.answer[:20])
