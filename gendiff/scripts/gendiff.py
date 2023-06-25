#!/usr/bin/env python3

import argparse
from gendiff import generate_diff
from gendiff import make_volume_string as stylish
from gendiff import make_plain as plain
from gendiff import make_json as json


def main():
    parser = argparse.ArgumentParser(
         description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', help='set format of output')
    args = parser.parse_args()
    if args.format == "stylish":
        formater = stylish
    elif args.format == "plain":
        formater = plain
    elif args.format == "json":
        formater = json
    print(generate_diff(args.first_file, args.second_file, formater))


if __name__ == "__main__":
    main()
