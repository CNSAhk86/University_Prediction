# predictions/utils.py

import tensorflow as tf

def load_model():
    return tf.keras.models.load_model('predictions/my_model.h5')

model = load_model()

university_inverse_mapping = {
    '서울대': 0,
    '고려대': 1,
    '연세대': 2,
    '서강대': 3,
    '성균관대': 4,
    '한양대': 5,
    '중앙대': 6,
    '경희대': 7,
    '이화여대': 8
}
