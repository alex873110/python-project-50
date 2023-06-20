from gendiff.formaters.stylish import make_volume_string


def diff(data_1, data_2):
    new_data = {}
    keys = list(data_1.keys() | data_2.keys())
    keys.sort()
    for key in keys:
        if key in data_1 and key in data_2:
            if isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
                # in case no diff between keys, add two blanks to key,
                # if additional data in second file, add '+' and blank to key,
                # if data deleted from first file, add '-' and blank to key
                new_data[f'  {key}'] = diff(data_1[key], data_2[key])
            elif data_1[key] == data_2[key]:
                new_data[f'  {key}'] = data_1[key]
            elif data_1[key] != data_2[key]:
                new_data[f'- {key}'] = data_1[key]
                new_data[f'+ {key}'] = data_2[key]
        elif key in data_1:
            new_data[f'- {key}'] = data_1[key]
        elif key in data_2:
            new_data[f'+ {key}'] = data_2[key]
    return new_data


def generate_diff(converted, format=make_volume_string):
    file1_data, file2_data = converted
    return format(diff(file1_data, file2_data))
