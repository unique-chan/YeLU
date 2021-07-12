import tensorflow as tf
from tensorflow.keras import layers

from loader import train_valid_test
from parser import parse_args


# Ref.
# https://github.com/taki0112/Tensorflow-DatasetAPI

args = parse_args()
train_valid_test('../data')