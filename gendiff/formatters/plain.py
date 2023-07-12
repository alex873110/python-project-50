from .constants import ADDED, REMOVED, UPDATED, NESTED


def to_str(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, str):
        return f"'{data}'"
    elif isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return data


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


def build_plain_text(tree, path=''):
    text = []
    statuses = [ADDED, REMOVED, UPDATED]
    for key, val in tree.items():
        if val['status'] == NESTED:
            text.append(build_plain_text(val['children'], (path + f'{key}.')))
        elif val['status'] in statuses:
            text.append(build_line(key, tree, path))
    text = '\n'.join(text)
    return text


def apply_plain(tree):
    return build_plain_text(tree)
