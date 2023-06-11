from gendiff.generate_diff  import generate_diff

def test_generate_diff():
    assert generate_diff(gendiff/files/file1.json, gendiff/files/file2.json) == "{\n
                         - follow: false\nhost: hexlet.io\n- proxy: 123.234.53.22\n
                         - timeout: 50\n+ timeout: 20\n+ verbose: true\n}"
