from django.db import models
from django.utils.translation import ugettext as _
import uuid

STATUS = (
    ('Active Full-time', 'AF'),
    ('Active Part-time', 'AP'),
    ('Laid Off', 'LO'),
    ('Retired', 'RT'),
    ('Terminated', 'TM'),
)


class Payment(models.Model):
    number_payment = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_payment = models.CharField(_('Name'), max_length=50, blank=True, null=True)
    date_payment = models.DateTimeField(_('date_payment'), auto_now_add=True)
    sum_payment = models.IntegerField(_('Sum'), blank=True, null=True)
    status_payment = models.CharField(max_length=20, choices=STATUS, default='AF')

    def __str__(self):
        return self.name_payment
