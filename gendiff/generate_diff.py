from gendiff.parser import open_and_parse
from gendiff.formaters.formater import use_formater
from .constants import ADDED, REMOVED, UNCHANGED, NESTED, UPDATED


def diff(data1, data2):
    keys = list(data1.keys() | data2.keys())
    removed_keys = list(data1.keys() - data2.keys())
    added_keys = list(data2.keys() - data1.keys())
    result = dict()
    keys.sort()
    for key in keys:
        if key in removed_keys:
            result[key] = {'status': REMOVED, 'value': data1[key]}
        elif key in added_keys:
            result[key] = {'status': ADDED, 'value': data2[key]}
        elif data1[key] == data2[key]:
            result[key] = {'status': UNCHANGED, 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {'status': NESTED,
                           'children': diff(data1[key], data2[key])}
        else:
            result[key] = {'status': UPDATED,
                           'value': {REMOVED: data1[key],
                                     ADDED: data2[key]}}
    return result


def generate_diff(file1_path, file2_path, format='stylish'):
    file1_data = open_and_parse(file1_path)
    file2_data = open_and_parse(file2_path)
    difference = diff(file1_data, file2_data)
    return use_formater(difference, format)
