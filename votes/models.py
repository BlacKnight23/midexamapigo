from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return 'Position: {}'.format(self.name)
        return 'Description: {}'.format(self.description)

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,related_name='posts', null=True)
    birthdate = models.DateField()
    platform = models.TextField()

    def __str__(self):
        return 'First Name: {}'.format(self.firstname)
        return 'Last Name: {}'.format(self.lastname)
        return 'Position: {}'.format(self.position)
        return 'Birthdate: {}'.format(self.birthdate)
        return 'Platform: {}'.format(self.platform)

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='posts')
    vote_datetime = models.TextField()
