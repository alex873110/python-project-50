import json
import yaml
from yaml.loader import SafeLoader


def convert(path):
    extension = str(path)[-4:]
    if extension == 'json':
        result = json.load(open(path))
    elif extension == 'yaml' or extension == '.yml':
        result = yaml.load(open(path), Loader=SafeLoader)
    return result
