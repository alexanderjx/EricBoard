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

        for i in eric_matrix:
            if self.first_name.lower() == i:
                return True
            elif i in self.first_name:
                return True
            else:
                return False
