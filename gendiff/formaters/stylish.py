from .constants import ADDED, REMOVED, UNCHANGED, UPDATED, NESTED

STATUSES = [ADDED, REMOVED, UNCHANGED]
MARK_SIZE = 2
BLANK_SIZE = 4


def built_indent(level, mark_size=0):
    indent = ' ' * (BLANK_SIZE * level - mark_size)
    return indent


def get_mark(status, level):
    mark = ''
    if status == ADDED:
        mark += '+ '
    elif status == REMOVED:
        mark += '- '
    elif status == UNCHANGED:
        mark += '  '
    indent = built_indent(level, MARK_SIZE)
    return f"{indent}{mark}"


def change_to_str(data):
    if isinstance(data, (int, bool)):
        return str(data).lower()
    elif data is None:
        return 'null'
    return data


def make_volume_data(data, level=1):
    indent = built_indent(level)
    previus_level_indent = built_indent(level - 1)
    result = ''
    if isinstance(data, dict):
        result += "{\n"
        for key, val in data.items():
            result += f"{indent}{key}: {make_volume_data(val, level + 1)}\n"
        result += f"{previus_level_indent}}}"
    else:
        result += f"{change_to_str(data)}"
    return result


def make_stylish(diff, level=1):
    indent = built_indent(level)
    prev_level_indent = built_indent(level - 1)
    result = ['{']
    for key, val in diff.items():
        status = val.get('status')
        if status == NESTED:
            children = val['children']
            result.append(f"{indent}{key}: "
                          f"{make_stylish(children, level + 1)}")
        elif status == UPDATED:
            added_and_removed_val = sorted(val['value'].keys(), reverse=True)
            for item in added_and_removed_val:
                value = val['value'][item]
                result.append(f"{get_mark(item, level)}{key}: "
                              f"{make_volume_data(value, level + 1)}")
        elif status in STATUSES:
            value = val['value']
            result.append(f"{get_mark(status, level)}{key}: "
                          f"{make_volume_data(value, level + 1)}")
    result.append(f"{prev_level_indent}}}")
    result = '\n'.join(result)
    return result
