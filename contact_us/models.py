from django.db import models

# Create your models here.

class contact_us(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    message = models.TextField()
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us Lists'


