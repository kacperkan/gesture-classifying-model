from . import downloader
from . import custom_objectives

import numpy as np
import cv2


class GestureClassifier(object):
    __CONFIG_FILE_URL = 'https://github.com/kacper1095/gesture_classifying_model/releases/download/0.1/config.yml'
    __OUT_KEY = 'gesture'
    __MODEL_URL_KEY = 'MODEL_URL'
    __MODEL_INFO = 'MODEL_INFO'
    __MAX_CONTEXT_SIZE_KEY = 'MAX_CONTENT_SIZE'
    __FRAMES_TO_OMMIT = 'FRAMES_TO_OMMIT'
    __IMAGE_INPUT_SHAPE_KEY = 'image_input_shape'

    def __init__(self):
        self.output = None
        self.config = downloader.download_config(GestureClassifier.__CONFIG_FILE_URL)
        self.out_key = GestureClassifier.__OUT_KEY
        self.context = []
        self.max_context_size = self.config[GestureClassifier.__MAX_CONTEXT_SIZE_KEY]
        self.frames_to_ommit = self.config[GestureClassifier.__FRAMES_TO_OMMIT]
        self.frames_ommitted = 0
        self.input_shape = self.config[GestureClassifier.__MODEL_INFO][GestureClassifier.__IMAGE_INPUT_SHAPE_KEY]
        self.image_width = self.input_shape[2]
        self.image_height = self.input_shape[1]

        self.model = self.load_model()

    def transform(self, X, **transform_params):
        if len(self.context) < self.max_context_size:
            if self.frames_ommitted == self.frames_to_ommit:
                self.context.append(X[-1])
                self.frames_ommitted = 0
            else:
                self.frames_to_ommit = 0
            return None

        inputs = X[-1]
        inputs = cv2.resize(inputs, (self.image_width, self.image_height))
        inputs = inputs.transpose((2, 0, 1)) / 255.
        prediction = self.model.predict(np.array([inputs]))[-1]
        self.output = prediction
        self.context.clear()
        return self.output

    def load_model(self):
        model = downloader.download_model(self.config[GestureClassifier.__MODEL_URL_KEY],
                                          self.config[GestureClassifier.__MODEL_INFO],
                                          custom_objectives={'f1': custom_objectives.f1}
                                          )
        return model
