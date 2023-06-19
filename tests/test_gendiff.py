from gendiff.generate_diff  import generate_diff
from gendiff.converter import convert

file = open('./tests/fixtures/expected.txt', 'r')
result_1 = file.read()
deepfile = open('./tests/fixtures/deepexpected.txt', 'r')
result_2 = deepfile.read()

adress1 = './tests/fixtures/file1.json'
adress2 = './tests/fixtures/file2.json' 
adress3 = './tests/fixtures/file3.yml'
adress4 = './tests/fixtures/file4.yaml'
converted1 = convert(adress1, adress2)
converted2 = convert(adress3, adress4)

def test_generate_diff():
    assert generate_diff(converted1) + '\n'  == result_1
    assert generate_diff(converted2) + '\n'  == result_1

deeppath1 = './tests/fixtures/deepfile1.json'
deeppath2 = './tests/fixtures/deepfile2.json'
deeppath3 = './tests/fixtures/deepfile1.yml'
deeppath4 = './tests/fixtures/deepfile2.yaml'
converted3 = convert(deeppath1, deeppath2)
converted4 = convert(deeppath3, deeppath4)

def test_generate_diff():
    assert generate_diff(converted3) + '\n'  == result_2
    assert generate_diff(converted4) + '\n'  == result_2
