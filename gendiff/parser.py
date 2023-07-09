import json
import yaml
import os.path
from yaml.loader import SafeLoader


def parse_content(content, format):
    if format == 'json':
        parsed_content = json.load(content)
    elif format == 'yaml' or 'yml':
        parsed_content = yaml.load(content, Loader=SafeLoader)
    else:
        raise ValueError('This format not supported. '
                         "Only 'yaml' and 'Json' formats supported")
    return parsed_content


def get_content(path):
    format = os.path.splitext(path)[1].strip('.')
    with open(path, 'r') as content:
        return parse_content(content, format)
