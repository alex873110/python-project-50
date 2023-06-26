import pytest
from gendiff.generate_diff import generate_diff

path1 = './tests/fixtures/file1.json'
path2 = './tests/fixtures/file2.json'
path3 = './tests/fixtures/file3.yml'
path4 = './tests/fixtures/file4.yaml'
path5 = './tests/fixtures/deepfile1.json'
path6 = './tests/fixtures/deepfile2.json'
path7 = './tests/fixtures/deepfile1.yml'
path8 = './tests/fixtures/deepfile2.yaml'

file = './tests/fixtures/expected.txt'
deepfile = './tests/fixtures/deepexpected.txt'
plainfile = './tests/fixtures/plainexpected.txt'
to_json_file = './tests/fixtures/tojsonexpected.json'


@pytest.mark.parametrize('input1,input2,expected',
                         [(path1, path2, file),
                          (path3, path4, file),
                          (path5, path6, deepfile),
                          (path7, path8, deepfile)])
def test_generate_diff(input1, input2, expected):
    result = open(expected, 'r').read()
    assert generate_diff(input1, input2) + '\n' == result


@pytest.mark.parametrize('file1,file2,expected,format',
                         [(path5, path6, plainfile, 'plain'),
                          (path7, path8, plainfile, 'plain'),
                          (path5, path6, to_json_file, 'json'),
                          (path7, path8, to_json_file, 'json')])
def test_generate_diff_with_formater(file1, file2, expected, format):
    result = open(expected, 'r').read()
    assert generate_diff(file1, file2, format) + '\n' == result
