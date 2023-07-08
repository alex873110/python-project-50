import json
import yaml
import os.path
from yaml.loader import SafeLoader


def parse_file(file_data, format):
    if format == 'json':
        parsed_data = json.load(file_data)
    elif format == 'yaml' or 'yml':
        parsed_data = yaml.load(file_data, Loader=SafeLoader)
    else:
        raise ValueError('This format not supported. '
                         "Only 'yaml' and 'Json' formats supported")
    return parsed_data


def open_and_parse(path):
    format = os.path.splitext(path)[1].strip('.')
    with open(path, 'r') as content:
        return parse_file(content, format)
