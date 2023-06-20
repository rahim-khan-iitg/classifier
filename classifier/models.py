from django.db import models
class image_db(models.Model):
    image=models.ImageField(upload_to="images",default="")