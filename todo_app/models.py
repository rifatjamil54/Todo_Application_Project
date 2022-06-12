from django.db import models

# Create your models here.

class Data(models.Model):
    data = models.CharField(max_length=100)

    class Meta:
        db_table = 'todo_data'

    def __str__(self):
        return self.data   
