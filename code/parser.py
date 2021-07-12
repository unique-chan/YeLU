import argparse
from util import parsed_arguments_dict


def parse_util(parser, verbose):
    args = parser.parse_args()
    if verbose:
        msg = parsed_arguments_dict(args)
        print(msg)
    return args


def parse_args(verbose=True):
    parser = argparse.ArgumentParser(description='github.com/unique-chan')
    # arguments
    parser.add_argument('--net', type=str, help='neural net name')
    parser.add_argument('--data', type=str, help='dataset path')
    parser.add_argument('--height', default=32, type=int, help='image height (default: 32)')
    parser.add_argument('--width', default=32, type=int, help='image width (default: 32)')
    parser.add_argument('--lr', default=.1, type=float, help='learning rate (default: 0.1)')
    parser.add_argument('--epochs', default=5, type=int, help='epochs (default: 0.1)')
    parser.add_argument('--batch_size', default=128, type=int, help='batch_size (default: 0.1)')
    parser.add_argument('--gpu_index', default=0, type=int, help='gpu_index (-1: cpu, 0 ~: gpu, default: 0)')
    # parse
    return parse_util(parser, verbose)

