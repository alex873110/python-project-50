import pytest
from gendiff.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = ''.join(f.readlines())
    return result


@pytest.mark.parametrize('file1_name,file2_name,expected,format',
                         [('file1.json', 'file2.json',
                           'result_stylish', ''),
                          ('file1.yml', 'file2.yml',
                           'result_stylish', ''),
                          ('file1.json', 'file2.json',
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
    if format == '':
        format = 'stylish'
    assert generate_diff(file1, file2, format) == result
