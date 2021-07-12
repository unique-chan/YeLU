from tensorflow import keras
from parser import parse_args


def train_valid_test(data_dir, args, train='train', valid='valid', test='test'):
    train_dir, valid_dir, test_dir =\
        '{}/{}'.format(data_dir, train), '{}/{}'.format(data_dir, valid), '{}/{}'.format(data_dir, test)
    train_dataset = keras.preprocessing.image_dataset_from_directory(directory=train_dir,
                                                                     batch_size=args.batch_size,
                                                                     image_size=(args.height, args.width),
                                                                     shuffle=True)
    valid_dataset = keras.preprocessing.image_dataset_from_directory(directory=valid_dir,
                                                                     batch_size=args.batch_size,
                                                                     image_size=(args.height, args.width),
                                                                     shuffle=False)
    test_dataset = keras.preprocessing.image_dataset_from_directory(directory=test_dir,
                                                                    batch_size=args.batch_size,
                                                                    image_size=(args.height, args.width),
                                                                    shuffle=False)
    return train_dataset, valid_dataset, test_dataset


