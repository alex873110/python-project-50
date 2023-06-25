#!/usr/bin/env python3

import argparse
from gendiff import generate_diff
# from gendiff import make_volume_string as stylish
# from gendiff import make_plain as plain
# from gendiff import make_json as json


def main():
    write_up = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=write_up)
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
