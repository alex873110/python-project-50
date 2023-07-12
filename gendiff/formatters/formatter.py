from gendiff.formatters.stylish import apply_stylish as stylish
from gendiff.formatters.plain import apply_plain as plain
from gendiff.formatters.json import apply_json as json


def apply_formatter(data, formater):
    if formater == 'stylish':
        return stylish(data)
    elif formater == 'plain':
        return plain(data)
    elif formater == 'json':
        return json(data)
    raise ValueError('This formater not supported. '
                     "Only 'plain','stylish' or "
                     "'json' formaters supported")
