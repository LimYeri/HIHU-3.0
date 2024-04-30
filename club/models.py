from django.db import models

# 동아리
class Club(models.Model):
    # 동아리이름
    name = models.CharField(max_length=200)
    # 모집기간
    period = models.TextField(null=True, blank=True)
    # 모집내용
    content = models.TextField()
    # 연락처
    contact = models.CharField(max_length=50, null=True, blank=True)
    # 모집인원
    number = models.TextField(null=True, blank=True)
    # 모집링크
    link = models.URLField(null=True, blank=True)
    # 이미지
    clubImg = models.ImageField(upload_to='images/club', null=True, blank=True)
    # 동아리 종류
    kind = models.CharField(max_length=30, null=True, blank=True)
    
    class Meta:
        db_table = 'clubs'
    
    def get_absolute_url(self):
        return f'/club/{self.pk}'
    
    def __str__(self):
        return self.name