from django.db import models

class SavedCoin(models.Model):
    coin = models.CharField(max_length=100)
    rate = models.FloatField()
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coin} - {self.rate}"
