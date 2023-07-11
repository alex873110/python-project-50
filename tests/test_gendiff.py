import pytest
from gendiff.generate_diff import generate_diff
import os
import json


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = ''.join(f.readlines())
    return result


@pytest.mark.parametrize('file1_name,file2_name,expected',
                         [('file1.json', 'file2.json', 'result_stylish'),
                          ('file1.yml', 'file2.yml', 'result_stylish')])
def test_generate_diff_default_formater(file1_name, file2_name, expected):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    result = read(get_fixture_path(expected))
    assert generate_diff(file1, file2) == result


@pytest.mark.parametrize('file1_name,file2_name,expected,format',
                         [('file1.json', 'file2.json',
                           'result_plain', 'plain'),
                          ('file1.yml', 'file2.yml',
                           'result_plain', 'plain'),
                          ('file1.json', 'file2.json',
                           'result_stylish', 'stylish'),
                          ('file1.yml', 'file2.yml',
                           'result_stylish', 'stylish')])
def test_generate_diff_plain_stylish(file1_name, file2_name, expected, format):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    result = read(get_fixture_path(expected))
    assert generate_diff(file1, file2, format) == result


@pytest.mark.parametrize('file1_name,file2_name',
                         [('file1.json', 'file2.json'),
                          ('file1.yml', 'file2.yml')])
def test_generate_diff_json_formater(file1_name, file2_name):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    diff = generate_diff(file1, file2, 'json')
    assert type(json.loads(diff)) == dict
