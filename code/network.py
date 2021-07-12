def model(network, pretrained=False):
    try:
        return eval(network + '({})'.format(pretrained))
    except Exception as e:
        print('[Error]', e)
        exit(1)


def MobileNetV1(pretrained=False):
    pass
    # pass

