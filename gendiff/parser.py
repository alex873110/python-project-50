import json
import yaml
import os.path
from yaml.loader import SafeLoader


def parse_content(content, extension):
    if extension == 'json':
        return json.load(content)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.load(content, Loader=SafeLoader)
    raise ValueError('This format not supported. '
                     "Only YAML and JSON formats supported")


def get_content(path):
    _, extension = os.path.splitext(path)
    with open(path, 'r') as content:
        return parse_content(content, extension[1:])
