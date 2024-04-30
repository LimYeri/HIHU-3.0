from django.db import models

# 주점
class Bar(models.Model):
    # 이름
    name = models.CharField(max_length=30)
    # 주소
    address = models.CharField(max_length=300)
    # 전화번호
    phone = models.CharField(max_length=20, null=True, blank=True)
    # 영업시간
    time = models.TextField(null=True, blank=True)
    # 이미지
    shopImg = models.ImageField(upload_to='images/bar', null=True, blank=True)
    # 위치링크
    link = models.URLField(null=True, blank=True)
    
    class Meta:
        db_table = 'bars'
    
    def get_absolute_url(self):
        return f'/bar/{self.pk}'
    
    def __str__(self):
        return self.name

# 주점 메뉴
class BarMenu(models.Model):
    # 메뉴 이름
    name = models.CharField(max_length=50)
    # 메뉴 종류
    type = models.CharField(max_length=50)
    # 가격
    price = models.IntegerField()
    # 어느 주점
    shop = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'barMenu'