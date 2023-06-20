
def change_bool(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            change_bool(value)
        elif isinstance(value, bool):
            dictionary[key] = str(value).lower()
        elif value is None:
            dictionary[key] = 'null'
    return dictionary


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


def stylish(data):
    change_bool(data)

    def walk(data, level):
        result = ''
        symbol = ('    ' * level)[:-2]
        last_blanks = ('    ' * level)
        if isinstance(data, dict):
            for key in data.keys():
                marks = ['+', '-', ' ']
                if key[0] not in marks:
                    symbol = ('    ' * level)
                value = data[key]
                if isinstance(data[key], dict):
                    result += f'\n{symbol}{key}: '
                    result += f'{{{walk(value, (level + 1))}\n{last_blanks}}}'
                else:
                    result += f'\n{symbol}{key}:'
                    if value:
                        result += f' {value}'
        return result
    return f'{{{walk(data, 1)}\n}}'


def generate_diff(converted, format=stylish):
    file1_data, file2_data = converted
    return format(diff(file1_data, file2_data))
