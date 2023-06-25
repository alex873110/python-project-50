from gendiff.generate_diff  import generate_diff
from gendiff.formaters.plain import make_plain
from gendiff.formaters.json import make_json

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


def test_generate_diff():
    assert generate_diff(path1, path2) + '\n'  == result_1
    assert generate_diff(path3, path4) + '\n'  == result_1
    assert generate_diff(path5, path6) + '\n' == result_2
    assert generate_diff(path7, path8) + '\n' == result_2
    assert generate_diff(path5, path6, make_plain) + '\n' == result_3
    assert generate_diff(path7, path8, make_plain) + '\n' == result_3
    assert generate_diff(path5, path6, make_json) + '\n' == result_4
    assert generate_diff(path7, path8, make_json) + '\n' == result_4
