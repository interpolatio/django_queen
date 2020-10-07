from django.db import models
import json


class Desk(models.Model):
    rank = models.CharField(max_length=300, unique = True)

    def set_rank(self, data):
        self.rank = json.dumps(data)

    def get_rank(self):
        return json.loads(self.rank)