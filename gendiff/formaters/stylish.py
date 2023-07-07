

def change_to_str(data):
    if isinstance(data, (int, bool)):
        return str(data).lower()
    elif data is None:
        return 'null'
    return data


def make_volume(data, level=1):
    symbol = ' ' * 4 * level
    old_symbol = ' ' * 4 * (level - 1)
    result = ''
    if isinstance(data, dict):
        result += "{\n"
        for key, val in data.items():
            result += f"{symbol}{key}: {make_volume(val, level + 1)}"
        result += f"{old_symbol}}}\n"
    else:
        result += f"{change_to_str(data)}\n"
    return result


def choice_mark(status):
    mark = ''
    if status == 'added':
        mark += '+ '
    elif status == 'removed':
        mark += '- '
    elif status == 'unchanged':
        mark += '  '
    return mark


def generate_stroke(dict_, key, level=1):
    blank_size = 4
    mark_size = 2
    symbol = ' ' * (blank_size * level - mark_size)
    result = ''
    val = dict_[key]
    result = ''
    status = val['status']
    if status == 'updated':
        items = sorted(val['value'].keys(), reverse=True)
        for item in items:
            result += f"{symbol}{choice_mark(item)}{key}: "
            result += f"{make_volume(val['value'][item], level + 1)}"
    elif status in ['added', 'removed', 'unchanged']:
        result += f"{symbol}{choice_mark(status)}{key}: "
        result += f"{make_volume(val['value'], level + 1)}"
    return result


def make_nested_dicts(diff_dicts, level=1):
    blank_size = 4
    last_symbol = ' ' * level * blank_size
    result = ''
    for key, val in diff_dicts.items():
        if val.get('children'):
            result += f"{last_symbol}{key}: {{\n"
            result += f"{make_nested_dicts(val['children'], level + 1)}"
            result += f"{last_symbol}}}\n"
        else:
            result += generate_stroke(diff_dicts, key, level)
    return result


def make_stylish(diff_dicts):
    return f"{{\n{make_nested_dicts(diff_dicts)}}}"
