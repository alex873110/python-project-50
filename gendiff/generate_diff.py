from gendiff.formaters.stylish import make_volume_string


def mark_key(data1, data2, key):
    keys = list(data1.keys() | data2.keys())
    only_in_data1_keys = list(data1.keys() - data2.keys())
    only_in_data2_keys = list(data2.keys() - data1.keys())
    keys.sort()
    if key in only_in_data1_keys:
        new_dict = {f'- {key}': data1[key]}
    elif key in only_in_data2_keys:
        new_dict = {f'+ {key}': data2[key]}
    elif data1[key] == data2[key]:
        new_dict = {f'  {key}': data1[key]}
    else:
        new_dict = {f'- {key}': data1[key], f'+ {key}': data2[key]}
    return new_dict


def is_dicts(dict1, dict2):
    return (isinstance(dict1, dict) and isinstance(dict2, dict))


def diff(data_1, data_2):
    new_data = {}
    keys = list(data_1.keys() | data_2.keys())
    common_keys = list(data_1.keys() & data_2.keys())
    keys.sort()
    for key in keys:
        if key in common_keys and is_dicts(data_1[key], data_2[key]):
            new_data[f'  {key}'] = diff(data_1[key], data_2[key])
        else:
            new_data.update(mark_key(data_1, data_2, key))
    return new_data


def generate_diff(converted, format=make_volume_string):
    file1_data, file2_data = converted
    return format(diff(file1_data, file2_data))
