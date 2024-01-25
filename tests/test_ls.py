from src.sh import sh


def test_ls1():
    pwd = sh.pwd()
    sh.cd("tests/data/")
    files = sh.ls()
    assert len(files) == 3
    assert files[0].name == "1.txt"
    assert files[0].size == 5

    assert files[1].name == "2.inc"
    assert files[1].size == 9

    assert files[2].name == "3.cfg"
    assert files[2].size == 0
    sh.cd(pwd)


def test_ls_filter():
    pwd = sh.pwd()
    sh.cd("tests/data/")
    files = sh.ls("*.inc")
    assert len(files) == 1
    sh.cd(pwd)
