# Gesture classifying model
## Introduction
Pip package used in sign language translation system available in the following repository:
***
[https://github.com/kacper1095/translation-system-application](https://github.com/kacper1095/translation-system-application)
***

## Installation

1. `pip install gesture_classifying_model`
2. At top of pipeline.py insert line 
    ```angular2html
    from gesture_classifying_model import GestureClassifier
    ```
3. Instantiate class in transfomers list, ex.:
    ```angular2html
    transformers = [
       AlreadyExistingTransfomer(),
       ...
       GestureClassifier(),
       ...
       AlreadyExistingTransfomer()
    ]
    ```
4. First run will cause download of weights to `models/gesture_classifier` with weights in *.h5 format and config.yml
5. Run appplication and start using system!

## Classifier input info
* image size = [None, 64, 64, 3] (batch size, height, width, channels)
    - where *None* means, it can be arbitrary number of frames, **only last frame is classified**
* values range = [0, 255] in RGB (may be float or int)

## Classifier ouput info
* only letters are classified
* available letters (both upper and lower)*:
```angular2html
abcdefghiklmnopqrstuwxy
```
* output size = [None, 24], where under *None* is same number as in the input

<small>*the reason for such letters is that 'j' and 'z' both need movement, but classifier uses only singular frames</small>


## Requirements
Used environment:
* Python 3.5
* Theano 0.9.0
* Keras 1.2.2

## Changelog
* v0.1.3:
    - documentation on PyPI

* v0.1.2:
    - first PyPI availability
     - downloading weights after one day, after next run
