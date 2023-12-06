from django.db import models


class Storage(models.Model):
    name = models.CharField()
    qty = models.IntegerField()

    class Meta:
        verbose_name = "storage"
        verbose_name_plural = "storage"

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)