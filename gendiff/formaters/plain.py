from .stylish import change_bool


def replace(something):
    if isinstance(something, dict):
        result = '[complex value]'
    elif something not in ['true', 'null', 'false']:
        result = f"'{something}'"
    else:
        result = something
    return result


def make_plain(data):
    change_bool(data)

    def walk(data, adress=""):
        result = ''
        for key in data.keys():
            value = data[key]
            replacer = replace(value)
            mark = str(key)[0]
            original_key = str(key)[2:]
            key2 = f'+ {original_key}'
            key1 = f'- {original_key}'
            plus = ' was added with value: '
            minus = ' was removed\n'
            update = ' was updated. From '
            if key == key1 and key1 in data and key2 in data:
                result += f"Property '{adress}{original_key}'{update}{replacer}"
                result += f" to {replace(data[key2])}\n"
            elif mark == ' ' and isinstance(value, dict):
                result += walk(value, (adress + f'{original_key}.'))
            elif mark == '+' and key1 not in data:
                result += f"Property '{adress}{original_key}'{plus}{replacer}\n"
            elif mark == '-':
                result += f"Property '{adress}{original_key}'{minus}"
        return result
    return walk(data)[:-1]
