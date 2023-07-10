import json
import yaml
import os.path
from yaml.loader import SafeLoader


def parse_content(content, format):
    if format == 'json':
        return json.load(content)
    elif format == 'yaml' or format == 'yml':
        return yaml.load(content, Loader=SafeLoader)
    raise ValueError('This format not supported. '
                     "Only 'yaml' and 'Json' formats supported")


def get_content(path):
    format = os.path.splitext(path)[1].strip('.')
    with open(path, 'r') as content:
        return parse_content(content, format)
