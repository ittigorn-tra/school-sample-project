from django.core.validators import MinValueValidator
from django.db import models


class Schools(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=20)
    max_student = models.IntegerField(
        default=50,
        validators=[
            MinValueValidator(0)
        ]
    )


class Students(models.Model):
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, primary_key=True)
    name_first = models.CharField(max_length=20)
    name_last = models.CharField(max_length=20)
