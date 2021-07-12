from tensorflow import keras


def train_test(args, train='train', test='test'):
    train_dir, test_dir =\
        '{}/{}'.format(args.data, train), '{}/{}'.format(args.data, test)
    train_dataset = keras.preprocessing.image_dataset_from_directory(directory=train_dir,
                                                                     batch_size=args.batch_size,
                                                                     image_size=(args.height, args.width),
                                                                     shuffle=True)
    test_dataset = keras.preprocessing.image_dataset_from_directory(directory=test_dir,
                                                                    batch_size=args.batch_size,
                                                                    image_size=(args.height, args.width),
                                                                    shuffle=False)
    return train_dataset, test_dataset


def train_valid_test(args, train='train', valid='valid', test='test'):
    train_dir, valid_dir, test_dir =\
        '{}/{}'.format(args.data, train), '{}/{}'.format(args.data, valid), '{}/{}'.format(args.data, test)
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


