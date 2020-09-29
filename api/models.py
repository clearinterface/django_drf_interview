from django.db import models

class Salaries(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    salary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salaries'
        verbose_name = 'salary'
        verbose_name_plural = 'salaries'
        ordering = ('id', 'name')

    def __str__(self):
        return self.name