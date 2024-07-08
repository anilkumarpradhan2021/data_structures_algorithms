import collections
import pathlib

import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

import tensorflow_datasets as tfds
#import tensorflow_text as tf_text


if __name__ == "__main__":
	print("Test1")
	data_url = 'https://storage.googleapis.com/download.tensorflow.org/data/stack_overflow_16k.tar.gz'

	dataset_dir = utils.get_file(
		origin=data_url,
		untar=True,
		cache_dir='stack_overflow',
		cache_subdir='')

	dataset_dir = pathlib.Path(dataset_dir).parent
	print(dataset_dir)

	print("Test1")