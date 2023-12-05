from django.db import models

class Todo(models.Model):

    title = models.CharField(max_length=50)
    description= models.CharField(max_length=200)
    data = models.CharField(max_length=50)
    img = models.ImageField(upload_to = 'Images',blank=True)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title