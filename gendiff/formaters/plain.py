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
    val = data[key]
    start = f"Property '{adress}{key}'"
    text = ''
    if val['status'] == UPDATED:
        text = f"{start} was updated. From {to_str(val['value'][REMOVED])}"
        text += f" to {to_str(val['value'][ADDED])}"
    elif val['status'] == REMOVED:
        text = f"{start} was removed"
    elif val['status'] == ADDED:
        text = f"{start} was added with value: {to_str(val['value'])}"
    return text


def make_plain(diff, adress=''):
    result = []
    status_list = [ADDED, REMOVED, UPDATED]
    for key, val in diff.items():
        if val['status'] == NESTED:
            result.append(make_plain(val['children'], (adress + f'{key}.')))
        elif val['status'] in status_list:
            result.append(build_stroke(key, diff, adress))
    result = '\n'.join(result)
    return result
