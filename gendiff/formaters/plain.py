from .stylish import change_bool


def replace(something):
    if isinstance(something, dict):
        result = '[complex value]'
    elif something in ['true', 'null', 'false'] or isinstance(something, int):
        result = something
    else:
        result = f"'{something}'"
    return result


def generate_text(key_, data_, path):
    plus = ' was added with value: '
    minus = ' was removed'
    update = ' was updated. From '
    value = data_[key_]
    replacer = replace(value)
    mark = str(key_)[0]
    original_key = str(key_)[2:]
    key2 = f'+ {original_key}'
    key1 = f'- {original_key}'
    start = f"Property '{path}{original_key}'"
    text = ''
    if key_ == key1 and key1 in data_ and key2 in data_:
        text = f"{start}{update}{replacer} to {replace(data_[key2])}\n"
    elif mark == '+' and key1 not in data_:
        text = f"{start}{plus}{replacer}\n"
    elif mark == '-':
        text = f"{start}{minus}\n"
    return text


def make_plain(data):
    change_bool(data)

    def walk(data, adress=""):
        result = ''
        for key in data.keys():
            if key[0] == ' ' and isinstance(data[key], dict):
                result += walk(data[key], (adress + f'{key[2:]}.'))
            else:
                result += generate_text(key, data, adress)
        return result
    return walk(data)[:-1]
