import main


def test_index():
    assert main.index() == 'Hello, world!'


def test_about():
    assert main.about() == 'This is the last assignment of Back-end'
