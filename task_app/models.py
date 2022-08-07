from tkinter.messagebox import NO
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    team = models.OneToOneField('Team', null=True, on_delete=models.SET_NULL, related_name='team')
    is_team_leader = models.BooleanField(default=False)
    



class Team(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    team_leader = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE, related_name='team_leader')
    # team_members = models.ForeignKey(User,on_delete=models.CASCADE,related_name='team_members' )

    def __str__(self):
        return self.name


class Task(models.Model):
    _STATUSES = (
        ("Assignd", "Assignd"),
        ("In progress", "In progress"),
        ("Under Review", "Under Review"),
        ("Done", "Done")
    )

    # id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False)
    assigned_team = models.OneToOneField(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_team')
    status = models.CharField(max_length=20, default=_STATUSES[0][0], choices=_STATUSES)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_team_members = models.ManyToManyField(User, related_name='assigned_users')
    created_by =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        # Override Save and dependency_value
        self.completed_at = None
        if self.status == self._STATUSES[1][0]:
            self.started_at = datetime.now() # In progress
        elif self.status == self._STATUSES[3][0]:
            if not self.started_at:
                self.started_at = datetime.now()
            self.completed_at = datetime.now() # Done
        elif self.status == self._STATUSES[0][0]:
            self.started_at = None
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name






class UserTaskMapper(models.Model):
    users = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tasks = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
