from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.
class Polls(models.Model) :
    poll_question = models.TextField()
    poll_option1 = models.CharField(max_length = 100)
    poll_option2 = models.CharField(max_length = 100)
    poll_option3 = models.CharField(max_length = 100)
    poll_option4 = models.CharField(max_length = 100)
    poll_option1_count = models.IntegerField(default = 0)
    poll_option2_count = models.IntegerField(default = 0)
    poll_option3_count = models.IntegerField(default = 0)
    poll_option4_count = models.IntegerField(default = 0)

class Voted(models.Model) :
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    poll = models.ForeignKey(Polls, on_delete = models.CASCADE)