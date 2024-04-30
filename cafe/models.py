from django.db import models

# 카페
class Cafe(models.Model):
    # 이름
    name = models.CharField(max_length=30)
    # 주소
    address = models.CharField(max_length=300)
    # 전화번호
    phone = models.CharField(max_length=20, null=True, blank=True)
    # 영업시간
    time = models.TextField(null=True, blank=True)
    # 이미지
    shopImg = models.ImageField(upload_to='images/cafe', null=True, blank=True)
    # 위치링크
    link = models.URLField(null=True, blank=True)
    
    class Meta:
        db_table = 'cafes'
    
    def get_absolute_url(self):
        return f'/cafe/{self.pk}'
    
    def __str__(self):
        return self.name


# 카페 메뉴
class CafeMenu(models.Model):
    # 메뉴 이름
    name = models.CharField(max_length=50)
    # 메뉴 종류
    type = models.CharField(max_length=50)
    # 가격
    price = models.IntegerField()
    # 어느 카페
    shop = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'cafeMenu'