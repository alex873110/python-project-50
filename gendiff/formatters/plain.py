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


def build_line(key, data, adress):
    value = data[key]
    start = f"Property '{adress}{key}'"
    if value['status'] == UPDATED:
        return (f"{start} was updated. From {to_str(value['value'][REMOVED])}"
                f" to {to_str(value['value'][ADDED])}")
    elif value['status'] == REMOVED:
        return f"{start} was removed"
    elif value['status'] == ADDED:
        return f"{start} was added with value: {to_str(value['value'])}"


def build_plain(diff, path=''):
    result = []
    statuses = [ADDED, REMOVED, UPDATED]
    for key, val in diff.items():
        if val['status'] == NESTED:
            result.append(build_plain(val['children'], (path + f'{key}.')))
        elif val['status'] in statuses:
            result.append(build_line(key, diff, path))
    result = '\n'.join(result)
    return result


def apply_plain(diff):
    return build_plain(diff)
