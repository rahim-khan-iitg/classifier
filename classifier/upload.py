import tensorflow as tf
import numpy as np
from requests import get
from tensorflow import keras ## model 1 and 2 uses sigmoid
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def handle_upload(f):
    with open("media/a.jpg","wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def download_model():
    with open("media/model.h5","wb") as file:
        response=get("https://rahimcdn.blob.core.windows.net/mycdn/model.h5")
        file.write(response.content)


@csrf_exempt
def predict():
    if not os.path.exists("media/model.h5"):
        download_model()
    model=keras.models.load_model("media/model.h5")
    img=keras.utils.load_img("media/a.jpg",target_size=(256,256))
    img_array=keras.utils.img_to_array(img)
    img_array=tf.expand_dims(img_array,0)
    pred=model.predict(img_array)
    x=np.argmax(tf.nn.softmax(pred[0]))
    if x==0:
        return "AI Generated"
    return "Real"

