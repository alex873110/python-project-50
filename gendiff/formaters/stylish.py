from .constants import ADDED, REMOVED, UNCHANGED, UPDATED, NESTED

STATUSES = {ADDED: '+ ', REMOVED: '- ', UNCHANGED: '  '}
MARK_SIZE = 2
BLANK_SIZE = 4


def built_indent(level, mark_size=0):
    indent = ' ' * (BLANK_SIZE * level - mark_size)
    return indent


def get_mark(status, level):
    mark = STATUSES[status]
    indent = built_indent(level, MARK_SIZE)
    return f"{indent}{mark}"


def generate_stroke(data, level=1):
    indent = built_indent(level)
    previus_level_indent = built_indent(level - 1)
    stroke = ''
    if isinstance(data, dict):
        nested_stroke = ["{"]
        for key, val in data.items():
            nested_stroke.append(f"{indent}{key}: "
                                 f"{generate_stroke(val, level + 1)}")
        nested_stroke.append(f"{previus_level_indent}}}")
        stroke += '\n'.join(nested_stroke)
    elif isinstance(data, (int, bool)):
        stroke += f"{str(data).lower()}"
    elif data is None:
        stroke += 'null'
    else:
        stroke += data
    return stroke


def make_volume_diff(diff, level=1):
    indent = built_indent(level)
    prev_level_indent = built_indent(level - 1)
    result = ['{']
    for key, val in diff.items():
        status = val.get('status')
        if status == NESTED:
            result.append(f"{indent}{key}: "
                          f"{make_volume_diff(val['children'], level + 1)}")
        elif status == UPDATED:
            added_and_removed_val = sorted(val['value'].keys(), reverse=True)
            for item in added_and_removed_val:
                result.append(
                   f"{get_mark(item, level)}{key}: "
                   f"{generate_stroke(val['value'][item], level + 1)}"
                )
        elif status in STATUSES:
            result.append(f"{get_mark(status, level)}{key}: "
                          f"{generate_stroke(val['value'], level + 1)}")
    result.append(f"{prev_level_indent}}}")
    result = '\n'.join(result)
    return result


def make_stylish(diff):
    return make_volume_diff(diff)
