from gendiff.generate_diff  import generate_diff

file = open('./tests/fixtures/expected.txt', 'r')
result_1 = file.read()

adress1 = './tests/fixtures/file1.json'
adress2 = './tests/fixtures/file2.json' 
def test_generate_diff():
    assert generate_diff(adress1, adress2) + '\n'  == result_1
