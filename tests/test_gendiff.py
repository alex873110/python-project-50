from gendiff.generate_diff  import generate_diff
from gendiff.parser import get_parsed

file = open('./tests/fixtures/expected.txt', 'r')
result_1 = file.read()

adress1 = './tests/fixtures/file1.json'
adress2 = './tests/fixtures/file2.json' 
adress3 = './tests/fixtures/file3.yml'
adress4 = './tests/fixtures/file4.yaml'
parsed1 = get_parsed(adress1, adress2)
parsed2 = get_parsed(adress3, adress4)

def test_generate_diff():
    assert generate_diff(parsed1) + '\n'  == result_1
    assert generate_diff(parsed2) + '\n'  == result_1
