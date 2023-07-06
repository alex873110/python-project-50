from gendiff.formaters.stylish import make_stylish as stylish
from gendiff.formaters.plain import make_plain as plain
from gendiff.formaters.json import make_json as json


def use_formater(data, format):
    if format == 'stylish':
        return stylish(data)
    elif format == 'plain':
        return plain(data)
    elif format == 'json':
        return json(data)
