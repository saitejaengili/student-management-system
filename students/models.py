from django.db import models

class Student(models.Model):
    YEAR_CHOICES = [
        ("1st Year", "1st Year"),
        ("2nd Year", "2nd Year"),
        ("3rd Year", "3rd Year"),
        ("4th Year", "4th Year"),
    ]

    roll_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=80)
    year = models.CharField(max_length=20, choices=YEAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["roll_number"]

    def __str__(self):
        return f"{self.roll_number} - {self.full_name}"
