from django.db import models
import tensorflow as tf

def load_model():
    model = tf.keras.models.load_model('predictions/my_model.h5')
    return model

model = load_model()