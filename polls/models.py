from django.db import models

# Create your models here.

class poll(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.IntegerField()
    active = models.BooleanField(default=True)
    total_voters = models.BigIntegerField(null=True)

class poll_option(models.Model):
    text = models.CharField(max_length=150)
    voter_n = models.BigIntegerField(default=0)
    Id_poll = models.ForeignKey(poll,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class voters(models.Model):
    name = models.CharField(max_length=150)
    Id_poll_option = models.ForeignKey(poll_option,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
