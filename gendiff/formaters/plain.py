from .constants import ADDED, REMOVED, UPDATED, NESTED


def to_str(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, str):
        return f"'{data}'"
    elif isinstance(data, (int, bool)):
        return str(data).lower()
    elif data is None:
        return 'null'


def build_stroke(key, data, adress):
    value = data[key]
    start = f"Property '{adress}{key}'"
    stroke = ''
    if value['status'] == UPDATED:
        stroke = f"{start} was updated. From {to_str(value['value'][REMOVED])}"
        stroke += f" to {to_str(value['value'][ADDED])}"
    elif value['status'] == REMOVED:
        stroke = f"{start} was removed"
    elif value['status'] == ADDED:
        stroke = f"{start} was added with value: {to_str(value['value'])}"
    return stroke


def make_plain(diff, adress=''):
    result = []
    statuses = [ADDED, REMOVED, UPDATED]
    for key, val in diff.items():
        if val['status'] == NESTED:
            result.append(make_plain(val['children'], (adress + f'{key}.')))
        elif val['status'] in statuses:
            result.append(build_stroke(key, diff, adress))
    result = '\n'.join(result)
    return result
