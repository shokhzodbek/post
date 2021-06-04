from django.db import models

class Post(models.Model):
      name = models.CharField(max_length=100,null=True,blank=True)
      post = models.TextField()

      def __str__(self) -> str:
          return self.name

# Create your models here.
