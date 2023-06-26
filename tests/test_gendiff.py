import pytest
from gendiff.generate_diff import generate_diff

file = open('./tests/fixtures/expected.txt', 'r')
result_1 = file.read()
deepfile = open('./tests/fixtures/deepexpected.txt', 'r')
result_2 = deepfile.read()
plainfile = open('./tests/fixtures/plainexpected.txt', 'r')
result_3 = plainfile.read()
to_json_file = open('./tests/fixtures/tojsonexpected.json', 'r')
result_4 = to_json_file.read()


path1 = './tests/fixtures/file1.json'
path2 = './tests/fixtures/file2.json'
path3 = './tests/fixtures/file3.yml'
path4 = './tests/fixtures/file4.yaml'
path5 = './tests/fixtures/deepfile1.json'
path6 = './tests/fixtures/deepfile2.json'
path7 = './tests/fixtures/deepfile1.yml'
path8 = './tests/fixtures/deepfile2.yaml'


@pytest.mark.parametrize('input1,input2,expected',
                         [(path1, path2, result_1),
                          (path3, path4, result_1),
                          (path5, path6, result_2),
                          (path7, path8, result_2)])
def test_generate_diff(input1, input2, expected):
    assert generate_diff(input1, input2) + '\n' == expected

#    assert generate_diff(path3, path4) + '\n' == result_1
#   assert generate_diff(path5, path6) + '\n' == result_2
#    assert generate_diff(path7, path8) + '\n' == result_2


@pytest.mark.parametrize('file1,file2,result,format', [(path5, path6, result_3, 'plain'),
                         (path7, path8, result_3, 'plain'), (path5, path6, result_4, 'json'),
                        (path7, path8, result_4, 'json')])
def test_generate_diff_with_formater(file1, file2, result, format):
    assert generate_diff(file1, file2, format) + '\n' == result

#    assert generate_diff(path5, path6, 'plain') + '\n' == result_3
#    assert generate_diff(path7, path8, 'plain') + '\n' == result_3
#    assert generate_diff(path5, path6, 'json') + '\n' == result_4
#    assert generate_diff(path7, path8, 'json') + '\n' == result_4
