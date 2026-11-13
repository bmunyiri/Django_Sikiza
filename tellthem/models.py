from datetime import date

from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_created = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."  # Display the first 50 characters of the entry