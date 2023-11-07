from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def is_eric(self):

        eric_matrix = [
            'erik', 'eric', 'erich',
            'erikk', 'erick', 'eirik',
            'eirikr', 'erikr', 'aeryk',
            'erk', 'eruc', 'eruk',
            'eruuc', 'eruuuc', 'eruuuuc',
            'eruuuuuc'
        ]

        if self.first_name.lower() in eric_matrix:
            return True

        else:
            return False
