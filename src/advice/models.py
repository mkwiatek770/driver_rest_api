from django.db import models


class Advice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    media = models.FilePathField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class WeekAdvice(models.Model):
    advice = models.OneToOneField(Advice, on_delete=models.CASCADE)

    def __str__(self):
        return self.advice.title
