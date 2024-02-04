from django.db import models

class YourModel(models.Model):
    #id = models.IntegerField(primary_key=True, verbose_name='ID')
    timestamp = models.CharField(max_length=20, verbose_name='Timestamp', db_index=True)
    turbidity = models.FloatField(verbose_name='Turbidity')
    temperature = models.FloatField(verbose_name='Temperature')
    pH = models.FloatField(verbose_name='pH')

    def __str__(self):
        return f"{self.id} - {self.timestamp}"
    
    class Meta:
        verbose_name = 'Your Model'
        verbose_name_plural = 'Your Models'