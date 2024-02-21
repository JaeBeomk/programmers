from django.db import models

# Create your models here.
# model 설계 후 migration 필수

class Post(models.Model):
    title = models.CharField("포스트제목",max_length=100)
    content = models.TextField("포스트 내용")
    thumbnail = models.ImageField("썸네일",upload_to="post",blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # FK 
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"
