import main


def test_index():
    assert main.index() == 'Hello, world!'
    #assert main.index() == 'failed test!'


def test_about():
    assert main.about() == 'This is the last assignment of Back-end'
