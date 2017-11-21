gesture-classifying-model
----------------

To use, first create GestureClassifier object::

    >>> predictor = GestureClassifier()

This may take a while as model is being downloaded and loaded (approx. 86 MB of weights).

After creation, you can use the predictor, by passing tensor of frames to transform function.
Numpy array of passed images should have same number of channels, same width and height.
GestureClassifier receives tensor in following shape (None, 64, 64, 3). By that I mean::

    >>> input_tensor.shape
    >>> (any_num, 64, 64, 3),

where 'any_num' is any number of frames passed. Images should be in range of values 0-255.

You can finally predict probabilities of frame of cropped hands (letters are indexed in order shown below)::

    >>> predictor.transform(input_tensor_of images)

Letters order::

     'abcdefghiklmnopqrstuvwxy' # alphabetical order for indices from 1 to 24 without