from gendiff.constants import ADDED, REMOVED, UNCHANGED, UPDATED
from gendiff.constants import STATUSES, BLANK_SIZE, MARK_SIZE


def get_spaces(level, mark_size=0):
    characters = ' ' * (BLANK_SIZE * level - mark_size)
    return characters


def get_mark(status, level):
    mark = ''
    if status == ADDED:
        mark += '+ '
    elif status == REMOVED:
        mark += '- '
    elif status == UNCHANGED:
        mark += '  '
    spaces = get_spaces(level, MARK_SIZE)
    return f"{spaces}{mark}"


def change_to_str(data):
    if isinstance(data, (int, bool)):
        return str(data).lower()
    elif data is None:
        return 'null'
    return data


def get_nested(data, level=1):
    characters = get_spaces(level)
    previus_level_characters = get_spaces(level - 1)
    result = ''
    if isinstance(data, dict):
        result += "{\n"
        for key, val in data.items():
            result += f"{characters}{key}: {get_nested(val, level + 1)}\n"
        result += f"{previus_level_characters}}}"
    else:
        result += f"{change_to_str(data)}"
    return result


def make_stylish(diff, level=1):
    characters = get_spaces(level)
    prev_level_characters = get_spaces(level - 1)
    result = ['{']
    for key, val in diff.items():
        status = val.get('status')
        if status == 'nested':
            children = val['children']
            result.append(f"{characters}{key}: "
                          f"{make_stylish(children, level + 1)}")
        elif status == UPDATED:
            items = sorted(val['value'].keys(), reverse=True)
            for item in items:
                value = val['value'][item]
                result.append(f"{get_mark(item, level)}{key}: "
                              f"{get_nested(value, level + 1)}")
        elif status in STATUSES:
            value = val['value']
            result.append(f"{get_mark(status, level)}{key}: "
                          f"{get_nested(value, level + 1)}")
    result.append(f"{prev_level_characters}}}")
    result = '\n'.join(result)
    return result
