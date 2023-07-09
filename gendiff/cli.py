import argparse


def parse_args():
    specification = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=specification)
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', help='set format of output')
    args = parser.parse_args()
    return args
