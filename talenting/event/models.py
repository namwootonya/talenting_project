from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from event.options import EVENT_CATEGORIES
from .countries import COUNTRIES


class EventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=1)
    event_categories = models.SmallIntegerField(_('categories'), choices=EVENT_CATEGORIES, default=1)
    title = models.CharField(max_length=20)
    program = models.TextField(max_length=300, blank=True)
    noted_item = models.TextField(max_length=100, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=2, choices=COUNTRIES)
    state = models.CharField(_('State/Region'), max_length=40, null=True, blank=True)
    city = models.CharField(_('City'), max_length=40)
    price = models.DecimalField(_('Price per person'), decimal_places=2, max_digits=6, blank=True, null=True)
    primary_photo = models.ImageField(upload_to='event')
    primary_photo_thumbnail = ImageSpecField(
        source='primary_photo',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
        )

    # Date
    opening_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField()
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Participants
    participants = models.ManyToManyField(
        'member.User',
        related_name='participants',
        blank=True,
        verbose_name='참여한 유저 목록'
    )
    maximum_participant = models.IntegerField(blank=True, null=True, default=0)
    participants_count = models.IntegerField(default=0, editable=False, blank=True)

    # Geo Location
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)

    objects = EventManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'

    def get_photos(self):
        photos = self.photo_set.all()
        return photos

    def participants_counter(self):
        participants = self.participants
        self.participants_count = participants

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)


class EventComment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    event = models.ForeignKey(Event, related_name='comments')
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

