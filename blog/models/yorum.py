from django.db import models
from django.contrib.auth.models import User

class YorumModel(models.Model):
    yazan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'