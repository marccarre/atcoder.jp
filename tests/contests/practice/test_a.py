import inspect
import pytest
from io import StringIO
from os.path import abspath, dirname, join
from contests.practice.a import main


def test_a_01(capsys, monkeypatch):
    expected_out = set_up(monkeypatch)
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_out


def test_a_02(capsys, monkeypatch):
    expected_out = set_up(monkeypatch)
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_out


def set_up(monkeypatch):
    test_name = inspect.stack()[1][3].replace('test_', '')
    directory = abspath(dirname(__file__))
    with open(join(directory, '%s_in.txt' % test_name), 'r') as f:
        monkeypatch.setattr('sys.stdin', StringIO(f.read()))
    with open(join(directory, '%s_out.txt' % test_name), 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    pytest.main()
