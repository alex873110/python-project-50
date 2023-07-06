from gendiff.converter import convert
from gendiff.formaters.formater import use_formater


def diff(data1, data2):
    keys = list(data1.keys() | data2.keys())
    only_in_data1_keys = list(data1.keys() - data2.keys())
    only_in_data2_keys = list(data2.keys() - data1.keys())
    result = dict()
    keys.sort()
    for key in keys:
        if key in only_in_data1_keys:
            result[key] = {'status': 'removed', 'value': data1[key]}
        elif key in only_in_data2_keys:
            result[key] = {'status': 'added', 'value': data2[key]}
        elif data1[key] == data2[key]:
            result[key] = {'status': 'unchanged', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {'status': 'changed',
                           'children': diff(data1[key], data2[key])}
        else:
            result[key] = {'status': 'updated',
                           'value': {'removed': data1[key],
                                     'added': data2[key]}}
    return result


def generate_diff(file1_path, file2_path, format='stylish'):
    file1_data, file2_data = convert(file1_path), convert(file2_path)
    difference = diff(file1_data, file2_data)
    return use_formater(difference, format)
