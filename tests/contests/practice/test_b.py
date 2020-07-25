import inspect
from os.path import abspath, dirname, join
from subprocess import Popen, PIPE
import pytest


DIR = abspath(dirname(__file__))
TIMEOUT_IN_SECS = 5


def test_b_01():
    psim, psol = set_up('practice')
    psim.wait(TIMEOUT_IN_SECS)
    psol.wait(TIMEOUT_IN_SECS)
    assert psim.returncode == 0, psim.stdout
    assert psol.returncode == 0, psol.stdout


def set_up(contest):
    test_name = inspect.stack()[1][3].replace('test_', '')
    with open(join(DIR, '%s_in.txt' % test_name), 'r') as f:
        _, max_queries = f.read().strip().split(' ')
    task = test_name.split('_')[0]
    simulator = join(DIR, 'interactive.py')
    psim = Popen(['python', simulator, test_name, max_queries], stdin=PIPE, stdout=PIPE)
    solution = abspath(join(DIR, '..', '..', '..', 'contests', contest, '%s.py' % task))
    psol = Popen(['python', solution], stdout=psim.stdin, stdin=psim.stdout)
    return psim, psol


if __name__ == '__main__':
    pytest.main()
