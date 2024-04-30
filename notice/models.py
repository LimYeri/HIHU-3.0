from django.db import models

# HIHU 공지
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=30)
    # 내용
    content = models.TextField()
    # 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 공지 이미지
    noticeImg = models.ImageField(upload_to='images/notice', null=True, blank=True)

    class Meta:
        db_table = 'posts'
    
    def get_absolute_url(self):
        return f'/notice/{self.pk}'
    
    def __str__(self):
        return self.title