def change_bool(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            change_bool(value)
        elif isinstance(value, bool):
            dictionary[key] = str(value).lower()
        elif value is None:
            dictionary[key] = 'null'
    return dictionary


def make_volume_string(data):
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
