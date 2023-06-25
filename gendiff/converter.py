import json
import yaml
from yaml.loader import SafeLoader


def convert(path1, path2):
    lst = [path1, path2]
    for index, item in enumerate(lst):
        extension = str(item)[-4:]
        if extension == 'json':
            lst[index] = json.load(open(item))
        elif extension == 'yaml' or extension == '.yml':
            lst[index] = yaml.load(open(item), Loader=SafeLoader)
    return tuple(lst)
