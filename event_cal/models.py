from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='event',null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
