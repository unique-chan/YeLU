from model.densenet import DenseNet


def network(args):
    try:
        return eval(args.net + '(num_classes={})'.format(args.num_classes))
    except Exception as e:
        print('[Error]', e)
        exit(1)


def densenet_121(num_classes):
    return DenseNet(num_classes, num_init_features=64, growth_rate=32, block_layers=[6, 12, 24, 16], compression_rate=0.5, drop_rate=0.5)


def densenet_169(num_classes):
    return DenseNet(num_classes, num_init_features=64, growth_rate=32, block_layers=[6, 12, 32, 32], compression_rate=0.5, drop_rate=0.5)


def densenet_201(num_classes):
    return DenseNet(num_classes, num_init_features=64, growth_rate=32, block_layers=[6, 12, 48, 32], compression_rate=0.5, drop_rate=0.5)


def densenet_264(num_classes):
    return DenseNet(num_classes, num_init_features=64, growth_rate=32, block_layers=[6, 12, 64, 48], compression_rate=0.5, drop_rate=0.5)