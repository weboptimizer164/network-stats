from __future__ import unicode_literals

from django.db import models

class Data(models.Model):
    Protocol = models.CharField(max_length=250)
    ListenAddress = models.CharField(max_length=250)
    ListenPort = models.CharField(max_length=250)
    RemoteAddress = models.CharField(max_length=250)
    RemotePort = models.CharField(max_length=250)
    Status = models.CharField(max_length=250)
    # ProcessId = models.CharField(max_length=250)
    # ProcessName = models.CharField(max_length=250)
    Time = models.TimeField()
    Date = models.DateField()
    # User = models.CharField(max_length=250)
    # Command = models.CharField(max_length=250)

class DataTemp(models.Model):
    Protocol = models.CharField(max_length=250)
    ListenAddress = models.CharField(max_length=250)
    ListenPort = models.CharField(max_length=250)
    RemoteAddress = models.CharField(max_length=250)
    RemotePort = models.CharField(max_length=250)
    Status = models.CharField(max_length=250)
    # ProcessId = models.CharField(max_length=250)
    # ProcessName = models.CharField(max_length=250)
    Time = models.TimeField()
    Date = models.DateField()
    # User = models.CharField(max_length=250)
    # Command = models.CharField(max_length=250)