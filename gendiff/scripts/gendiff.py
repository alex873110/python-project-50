#!/usr/bin/env python3

import argparse
from gendiff import generate_diff
from gendiff import convert
from gendiff import make_volume_string as stylish


def main():
    parser = argparse.ArgumentParser(
         description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str,
                        default=stylish, help='set format of output')
    args = parser.parse_args()
    converted = convert(args.first_file, args.second_file)
    print(generate_diff(converted, args.format))


if __name__ == "__main__":
    main()
