from .constants import ADDED, REMOVED, UPDATED, NESTED


def modify(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, str):
        return f"'{data}'"
    elif isinstance(data, (int, bool)):
        return str(data).lower()
    elif data is None:
        return 'null'


def generate_stroke(key_, data_, adress_):
    val_ = data_[key_]
    start = f"Property '{adress_}{key_}'"
    text = ''
    if val_['status'] == UPDATED:
        text = f"{start} was updated. From {modify(val_['value'][REMOVED])}"
        text += f" to {modify(val_['value'][ADDED])}\n"
    elif val_['status'] == REMOVED:
        text = f"{start} was removed\n"
    elif val_['status'] == ADDED:
        text = f"{start} was added with value: {modify(val_['value'])}\n"
    return text


def make_plain(diff):
    def walk(diff, adress=''):
        result = ''
        status_list = [ADDED, REMOVED, UPDATED]
        for key, val in diff.items():
            if val['status'] == NESTED:
                result += walk(val['children'], (adress + f'{key}.'))
            elif val['status'] in status_list:
                result += generate_stroke(key, diff, adress)
        return result
    return walk(diff)[:-1]
