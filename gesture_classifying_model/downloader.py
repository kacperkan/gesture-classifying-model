import wget
import yaml
from keras.models import load_model
import os
import numpy as np
import shutil
import time

WEIGHTS_FOLDER = os.path.join('models', 'gesture_classifier')
CONFIG_FILE = os.path.join(WEIGHTS_FOLDER, 'config.yml')
WEIGHTS_FILE = os.path.join(WEIGHTS_FOLDER, 'weights.h5')


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def download_config(config_file_url):
    config_filename = wget.download(config_file_url)
    ensure_dir(WEIGHTS_FOLDER)
    shutil.move(config_filename, CONFIG_FILE)
    with open(CONFIG_FILE, 'r') as conf_file:
        conf = yaml.load(conf_file)
    return conf


def download_model(weight_url, models_info, custom_objectives=None):
    return __initialize_model(__download_model(weight_url, custom_objectives), models_info['image_input_shape'])


def __download_model(weights_url, custom_objectives=None):
    now = time.time()
    one_day_ago = 60*60*24
    if not os.path.exists(WEIGHTS_FILE) or now - os.path.getmtime(WEIGHTS_FILE) > one_day_ago:
        weights_filename = wget.download(weights_url)
        ensure_dir(WEIGHTS_FOLDER)
        shutil.move(weights_filename, WEIGHTS_FILE)
    model = load_model(WEIGHTS_FILE, custom_objects=custom_objectives)
    return model


def __initialize_model(model, image_input_shape):
    _ = model.predict(np.array([np.zeros(image_input_shape)]))[0]
    return model
