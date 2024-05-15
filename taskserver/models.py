from django.db import models
from users.models import user
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ])
    assignee = models.ForeignKey(user, on_delete=models.CASCADE)
    # dependencies = models.ManyToManyField('self', blank=True)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    

    def __str__(self):
        return self.title