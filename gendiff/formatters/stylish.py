from .constants import ADDED, REMOVED, UNCHANGED, UPDATED, NESTED

STATUSES = {ADDED: '+ ', REMOVED: '- ', UNCHANGED: '  '}
MARK_SIZE = 2
BLANK_SIZE = 4


def built_indent(level, mark_size=0):
    indent = ' ' * (BLANK_SIZE * level - mark_size)
    return indent


def get_mark(status, level):
    mark = STATUSES[status]
    indent = built_indent(level, MARK_SIZE)
    return f"{indent}{mark}"


def convert_to_str(data, level=1):
    if isinstance(data, dict):
        indent = built_indent(level)
        previus_level_indent = built_indent(level - 1)
        nested_text = ["{"]
        for key, val in data.items():
            nested_text.append(f"{indent}{key}: "
                               f"{convert_to_str(val, level + 1)}")
        nested_text.append(f"{previus_level_indent}}}")
        return '\n'.join(nested_text)
    elif isinstance(data, bool):
        return f"{str(data).lower()}"
    elif data is None:
        return 'null'
    else:
        return f"{data}"


def build_stylish_tree(tree, level=1):
    indent = built_indent(level)
    prev_level_indent = built_indent(level - 1)
    result = ['{']
    for key, val in tree.items():
        node_status = val.get('status')
        if node_status == NESTED:
            result.append(f"{indent}{key}: "
                          f"{build_stylish_tree(val['children'], level + 1)}")
        if node_status == UPDATED:
            added_and_removed_val = val['value'].keys()
            for item in added_and_removed_val:
                result.append(
                    f"{get_mark(item, level)}{key}: "
                    f"{convert_to_str(val['value'][item], level + 1)}"
                )
        if node_status in STATUSES:
            result.append(f"{get_mark(node_status, level)}{key}: "
                          f"{convert_to_str(val['value'], level + 1)}")
    result.append(f"{prev_level_indent}}}")
    result = '\n'.join(result)
    return result


def apply_stylish(tree):
    return build_stylish_tree(tree)
