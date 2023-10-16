from django.db import models

# Create your models here.

WEEK_DAY = {
    "Monday": "Monday", 
    "Tuesday": "Tuesday",
    "Wednesday": "Wednesday", 
    "Thursday": "Thursday", 
    "Friday": "Friday",
    "Saturday": "Saturday",
    "Sunday": "Sunday",
}
WEEK_DAY = [
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
    ]

class Ticket(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    sub_title = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    valute = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    day_of_week = models.CharField(max_length=40, choices=WEEK_DAY, null=True, blank=True)
    mounth_and_day = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    address_second = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    href = models.CharField(max_length=300)


    def __str__(self):
        return self.title
