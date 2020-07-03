from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    studentid=models.CharField(max_length=50)
    age=models.CharField(max_length=20)
    section=models.CharField(max_length=20)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name