from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Indicators(models.Model):
    V = models.FloatField()
    A = models.FloatField()
    W = models.FloatField()
    socket_id = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)


class On_Off_google(models.Model):
    on_off = models.CharField(max_length=30)


class On_Off(models.Model):
    on_off = models.FloatField(default=0)
    user = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
