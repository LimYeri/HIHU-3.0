from django.db import models

# class VisitorCount(models.Model):
#     visit_date = models.CharField(primary_key=True, max_length=45)
#     visit_count = models.IntegerField(blank=True, null=True)

# 메인 페이지 배너
class Banner(models.Model):
    # 메인 텍스트
    main_text = models.TextField()
    # 위 서브 텍스트
    sub_text_1 = models.TextField(null=True, blank=True)
    # 아래 서브 텍스트
    sub_text_2 = models.TextField(null=True, blank=True)
    # 이미지
    img = models.ImageField(upload_to='images/banner')
    
    def __str__(self):
        return self.main_text