from django.db import models

# HIHU 일정
class Schedule(models.Model):
    # 시작일 
    startDate = models.DateField()
    # 마감일
    endDate = models.DateField()
    # 일정
    event = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'schedules'
    
    def __str__(self):
        return self.event