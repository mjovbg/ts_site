from django.db import models

# Create your models here.
# DB in django are in classes
# it is always 2-step process: 1) create model; 2) migrate it
# commands for migrations: 1) python manage.py makemigrations; 2) python manage.py migrate

class Stock(models.Model):
    # now define DB - what you want to save:
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker


