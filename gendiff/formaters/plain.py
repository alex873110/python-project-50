

def modify(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, str):
        return f"'{data}'"
    elif isinstance(data, (int, bool)):
        return str(data).lower()
    elif data is None:
        return 'null'


def generate_text(key_, data_, adress_):
    val_ = data_[key_]
    start = f"Property '{adress_}{key_}'"
    text = ''
    if val_['status'] == 'updated':
        text = f"{start} was updated. From {modify(val_['value']['removed'])}"
        text += f" to {modify(val_['value']['added'])}\n"
    elif val_['status'] == 'removed':
        text = f"{start} was removed\n"
    elif val_['status'] == 'added':
        text = f"{start} was added with value: {modify(val_['value'])}\n"
    return text


def make_plain(diff):
    def walk(diff, adress=''):
        result = ''
        status_list = ['updated', 'removed', 'added']
        for key, val in diff.items():
            if val['status'] == 'nested':
                result += walk(val['children'], (adress + f'{key}.'))
            elif val['status'] in status_list:
                result += generate_text(key, diff, adress)
        return result
    return walk(diff)[:-1]
