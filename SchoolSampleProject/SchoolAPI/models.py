from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class School(models.Model):
    school_name = models.CharField(max_length=20)
    max_student_count = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(50),
            MinValueValidator(0)
        ]
    )


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    name_first = models.CharField(max_length=20)
    name_last = models.CharField(max_length=20)
