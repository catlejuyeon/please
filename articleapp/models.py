from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)  # 작성자만 삭제
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)  # 데이터베이스에서 auto_now_add를 해야 작성한 날짜가 기록됨.

    like = models.IntegerField(default=0)   #좋아요
    wondering = models.IntegerField(default=0)  #궁금해요
