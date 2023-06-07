import json

def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    dict1 = dict(sorted(file1.items()))
    dict2 = dict(sorted(file2.items()))
    result =''
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
