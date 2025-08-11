from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  # Student's name
    age = models.IntegerField()              # Student's age
    email = models.EmailField(unique=True)   # Student's email (must be unique)

    def _str_(self):
        return self.name