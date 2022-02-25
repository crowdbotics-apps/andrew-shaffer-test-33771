from django.conf import settings
from django.db import models


class App(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    
    WEB = 'Web'
    MOBILE = 'Mobile'
    
    TYPE_CHOICES = (
        (WEB, 'Web'),
        (MOBILE, 'Mobile')
    )

    type = models.CharField(max_length=6, choices=TYPE_CHOICES)

    DJANGO = 'Django'
    REACT = 'React Native'
    
    FRAMEWORK_CHOICES = (
        (DJANGO, 'Django'),
        (REACT, 'React Native')
    )
    
    framework = models.CharField(max_length=12, choices=FRAMEWORK_CHOICES)

    domain_name = models.CharField(max_length=50, blank=True)
    screenshot = models.URLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='apps', on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.type}, {self.framework}'

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriptions', on_delete=models.CASCADE)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    app = models.OneToOneField(App, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.app.name} - {self.plan}'

class Plan(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(decimal_places=0, max_digits=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - ${self.price}'
