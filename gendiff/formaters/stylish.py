def change_bool(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            change_bool(value)
        elif isinstance(value, bool):
            dictionary[key] = str(value).lower()
        elif value is None:
            dictionary[key] = 'null'
    return dictionary


def generate_stroke(key, value, level):
    mark_size = 2
    marks = ['+', '-', ' ']
    if key[0] not in marks:
        mark_size = 0
    significant = ' '
    # according to task for each level indent = 4 symbols
    symbols_quantity = 4 * level - mark_size
    symbols = symbols_quantity * significant
    if isinstance(value, dict):
        stroke = f'\n{symbols}{key}:'
    else:
        stroke = f'\n{symbols}{key}:'
        if value:
            stroke += f' {value}'
    return stroke


def make_volume_string(data):
    change_bool(data)

    def walk(data, level):
        result = ''
        last_blanks = ('    ' * level)
        for key in data.keys():
            value = data[key]
            if isinstance(data[key], dict):
                result += generate_stroke(key, value, level)
                result += f' {{{walk(value, (level + 1))}\n{last_blanks}}}'
            else:
                result += generate_stroke(key, value, level)
        return result

    return f'{{{walk(data, 1)}\n}}'
