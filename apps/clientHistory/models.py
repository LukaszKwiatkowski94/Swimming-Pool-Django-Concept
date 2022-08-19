from django.db import models
from apps.user.models import User
from apps.offers.models import Passes
import datetime

class ClientHistoryPasses(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="User")
    passID = models.ForeignKey(Passes, on_delete = models.CASCADE, verbose_name="Pass")
    dateStart = models.DateField(default=datetime.date.today, verbose_name="Date Start")
    dateEnd = models.DateField(verbose_name="Date End")