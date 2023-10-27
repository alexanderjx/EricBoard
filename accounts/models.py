from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def is_eric(self):
        for i in ['Erik', 'Eric', 'Erich', 'Erikk', 'Erick', 'Eirik', 'Eirikr', 'Erikr', 'Aeryk', 'Erk']:
            if self.first_name == i:
                return True
            elif i in self.first_name:
                return True
            else:
                return False
