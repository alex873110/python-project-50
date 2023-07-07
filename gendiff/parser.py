import json
import yaml
from yaml.loader import SafeLoader


def choice_format(path):
    extension = str(path)[-4:]
    if extension == 'json':
        format = 'json'
    elif extension == 'yaml' or extension == '.yml':
        format = 'yaml'
    else:
        raise ValueError('This format not supported. '
                         "Only 'yaml' and 'Json' formats supported")
    return format


def parse_file(file_data, format):
    if format == 'json':
        parsed_data = json.load(file_data)
    elif format == 'yaml':
        parsed_data = yaml.load(file_data, Loader=SafeLoader)
    return parsed_data


def open_and_parse(path):
    format = choice_format(path)
    with open(path, 'r') as content:
        return parse_file(content, format)
