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

    def walk(data, path=""):
        result = ''
        for key in data.keys():
            value = data[key]
            replacer = replace(value)
            mark = str(key)[0]
            original = str(key)[2:]
            key2 = f'+ {original}'
            key1 = f'- {original}'
            plus = ' was added with value: '
            minus = ' was removed\n'
            update = ' was updated. From '
            if key1 in data and key2 in data:
                if key == key1:
                    result += f"Property '{path}{original}'{update}"
                    result += f"{replacer} to {replace(data[key2])}\n"
            elif mark == ' ':
                if isinstance(value, dict):
                    result += walk(value, (path + f'{original}.'))
            elif mark == '+':
                if isinstance(value, dict):
                    result += f"Property '{path}{original}'{plus}{replacer}\n"
                else:
                    result += f"Property '{path}{original}'{plus}{replacer}\n"
            elif mark == '-':
                if isinstance(value, dict):
                    result += f"Property '{path}{original}'{minus}"
                else:
                    result += f"Property '{path}{original}'{minus}"
        return result
    return walk(data)[:-1]
