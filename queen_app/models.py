from django.db import models
from django.db import IntegrityError
import json


class Desk(models.Model):
    rank = models.CharField(max_length=300, unique=True)

    def save(self, *args, **kwargs):
        try:
            super(Desk, self).save(*args, **kwargs)
        except IntegrityError:
            pass

    def set_rank(self, data):
        self.rank = json.dumps(data)

    def get_rank(self):
        return json.loads(self.rank)