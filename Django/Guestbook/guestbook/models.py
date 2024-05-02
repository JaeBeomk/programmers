from django.db import models
from django.utils import timezone

# Create your models here.
# 방명록 모델
class Guestbook(models.Model):
    title = models.CharField(max_length=100,null=False) # title에 null값 false 안주면 에러남
    name = models.CharField(max_length=20,null=False)
    contents = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    reg_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Guestbook({self.name},{self.title},{self.contents},{self.create_date},{self.reg_date})'