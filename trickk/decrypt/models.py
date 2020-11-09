from django.db import models
from .utils import get_filtered_image
import PIL.Image
import numpy as np
import cv2
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.
class decrypt(models.Model):
    encrypted_image=models.ImageField()
    result=models.ImageField(null=True, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classfied at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))
    
    def save(self, *args, **kwargs):
        pil_img=PIL.Image.open(self.encrypted_image)
        
        cv_img=np.array(pil_img)

        ###
        img=get_filtered_image(cv_img)
        ###

        img_pil=PIL.Image.fromarray(img)

        buffer=BytesIO()
        img_pil.save(buffer, format='png')
        image_png=buffer.getvalue()
        self.result.save(str (self.result), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)