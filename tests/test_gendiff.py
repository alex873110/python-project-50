import pytest
from gendiff.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize('file1_name,file2_name,expected',
                         [('file1.json', 'file2.json', 'expected.txt'),
                          ('file1.yml', 'file2.yaml', 'expected.txt'),
                          ('deepfile1.json', 'deepfile2.json',
                           'deepexpected.txt'),
                          ('deepfile1.yml', 'deepfile2.yaml',
                           'deepexpected.txt')])
def test_generate_diff(file1_name, file2_name, expected):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    result = read(get_fixture_path(expected))[:-1]
    assert generate_diff(file1, file2)  == result


@pytest.mark.parametrize('file1_name,file2_name,expected,format',
                         [('deepfile1.json', 'deepfile2.json',
                           'plainexpected.txt', 'plain'),
                          ('deepfile1.yml', 'deepfile2.yaml',
                           'plainexpected.txt', 'plain'),
                          ('deepfile1.json', 'deepfile2.json',
                           'tojsonexpected.json', 'json'),
                          ('deepfile1.yml', 'deepfile2.yaml',
                           'tojsonexpected.json', 'json')])
def test_generate_diff_with_formater(file1_name, file2_name, expected, format):
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    result = read(get_fixture_path(expected))[:-1]
    assert generate_diff(file1, file2, format)  == result
