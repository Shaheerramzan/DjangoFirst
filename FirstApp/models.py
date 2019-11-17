from django.db import models


# Create your models here.
class Profile(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=100, null=True, blank=True)
    year_of_graduation = models.IntegerField()


class Students(models.Model):
    name = models.CharField(max_length=50)
    roll_num = models.IntegerField(default=0)
    sec = models.CharField(max_length=100, null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.roll_num)


class ResultCard(models.Model):
    marks = models.IntegerField
    is_passed = models.BooleanField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='results')
