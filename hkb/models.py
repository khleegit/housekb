from django.db import models
from django.utils import timezone

class Classification(models.Model):
    cf01 = models.CharField(max_length=5)
    cf02 = models.CharField(max_length=200)
    cf03 = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(blank=True, null=True)

    def edited(self):
        self.edited_date = timezone.now()
        self.save()
