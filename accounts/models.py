from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # Add additional fields here.

    def __str__(self):
        return self.username
