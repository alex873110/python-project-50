import json


def make_json(data):
    json_stroke = json.dumps(data, indent=2)
    return json_stroke
