import json
import yaml
from yaml.loader import SafeLoader


def change_bool(dict):
    for key, value in dict.items():
        if type(value) == bool:
            if value is True:
                dict[key] = 'true'
            elif value is False:
                dict[key] = 'false'
    return dict


def get_parsed(path1, path2):
    lst = [path1, path2]
    for index, item in enumerate(lst):
        extension = str(item)[-4:]
        if extension == 'json':
            lst[index] = json.load(open(item), object_hook=change_bool)
        elif extension == 'yaml' or extension == '.yml':
            lst[index] = yaml.load(open(item), Loader=SafeLoader)
    return tuple(lst)
