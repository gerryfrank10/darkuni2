from django.db import models

# Create your models here.
class ContactModel(models.Model):
    UNIVERSITY_CHOICES = [
        ('ARDHI', 'Ardhi university'),
        ('UDSM', 'University of Dar-es-salaam'),
        ('KIUT', 'Kampala University'),
        ('CBE', 'College of Bussiness'),
        ('ATC', 'Arusha Technicall college'),
        ('SUA', 'Saut University'),
        ('SOKOINE', 'Sokoine University'),
        ('UDOM', 'University of Dodoma'),
        ('DIT','Dar-es-salaam institute of technology'),
        ('TUM','Tumaini University'),
        ('DUCE','Duce University'),
    ]
    
    name = models.CharField(max_length=100, help_text="Enter the name")
    email = models.EmailField(max_length=100, help_text="Enter the mail")
    university = models.CharField(max_length=10, choices=UNIVERSITY_CHOICES, default='CBE')
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name