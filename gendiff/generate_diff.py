
def change_bool(dict):
    for key, value in dict.items():
        if type(value) == bool:
            if value is True:
                dict[key] = 'true'
            elif value is False:
                dict[key] = 'false'
    return dict


def generate_diff(parsed):
    file1, file2 = parsed
    dict1 = dict(sorted(file1.items()))
    dict1 = change_bool(dict1)
    dict2 = dict(sorted(file2.items()))
    dict2 = change_bool(dict2)
    result = ''
    for key in dict1:
        if key in dict2:
            if dict1[key] == dict2[key]:
                result += f'  {key}: {dict1[key]}\n'
            else:
                result += f'- {key}: {dict1[key]}\n'
                result += f'+ {key}: {dict2[key]}\n'
        else:
            result += f'- {key}: {dict1[key]}\n'
    for key2 in dict2:
        if key2 not in dict1:
            result += f'+ {key2}: {dict2[key2]}\n'
    result = '{\n' + result + '}'
    return result
