from email.policy import default
from django.db import models
from django.contrib.auth.models import User # django handles for us user name, 
                                            #e-mail, password etc.

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)# user name
    title = models.CharField(max_length=200) # name of task in todo list
    description = models.TextField(null=True, blank=True) #text of task/item
    complete = models.BooleanField(default=False) #boolean (complete or not True - False)
    create = models.DateTimeField(auto_now_add=True) # time of creating task Data and time

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']