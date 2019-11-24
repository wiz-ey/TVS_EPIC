from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    vehicle_model = models.CharField(max_length=200)
    vehicle_age = models.CharField(max_length=200, default='1 year')
    vehicle_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    active_status = models.BooleanField(default = True)
    vehicle_km = models.IntegerField()
    text = models.TextField()
    vr_image = models.ImageField(upload_to='vr_uploads/%Y/%m/%d/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def activate(self):
        self.active_status = True
        self.save()

    def deactivate(self):
        self.active_status = False
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Bids(models.Model):
    post = models.ForeignKey('portal.Post', on_delete=models.CASCADE, related_name='bids')
    bidder = models.CharField(max_length=200)
    bid_amount = models.IntegerField()

    def get_absolute_url(self):
        return reverse('post_list')

    def publish(self):
        self.save()

    def __str__(self):
        return self.bidder
