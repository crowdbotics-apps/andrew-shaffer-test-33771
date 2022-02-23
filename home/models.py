from django.conf import settings
from django.db import models


class App(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    
    WEB = 'WEB'
    MOBILE = 'MOBILE'
    
    TYPE_CHOICES = (
        (WEB, 'Web'),
        (MOBILE, 'Mobile')
    )

    type = models.CharField(max_length=6, choices=TYPE_CHOICES)

    DJANGO = 'DJANGO'
    REACT = 'REACT'
    
    FRAMEWORK_CHOICES = (
        (DJANGO, 'Django'),
        (REACT, 'React Native')
    )
    
    framework = models.CharField(max_length=6, choices=FRAMEWORK_CHOICES)

    domain_name = models.CharField(max_length=50)
    screenshot = models.URLField()
    # subscription = models.ForeignKey('Subscription', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='apps', on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriptions', on_delete=models.CASCADE)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    app = models.ForeignKey('App', on_delete=models.CASCADE)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Plan(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(decimal_places=0, max_digits=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
