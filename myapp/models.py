from django.db import models

# Create your models here.
class todo(models.Model):
    head = models.CharField(max_length = 100,blank=False)
    create = models.DateTimeField(auto_now_add=True,blank=False)
    content = models.TextField()

    def __str__(self):
        return self.head