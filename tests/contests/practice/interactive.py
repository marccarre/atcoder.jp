from os.path import abspath, dirname, join
import sys


DIR = abspath(dirname(__file__))


def main(test_name, max_queries):
    inputs = _read_inputs(test_name)
    mappings = _read_mappings(test_name)
    solution = _read_solution(test_name)
    print(inputs, flush=True)
    for _ in range(int(max_queries)):
        i = input().strip()
        if i.startswith('?'):
            print(mappings[i], flush=True)
        elif i == solution:
            sys.exit(0)
        else:
            raise ValueError(i)
    raise RuntimeError('Too many queries')


def _read_inputs(test_name):
    with open(join(DIR, '%s_in.txt' % test_name), 'r') as f:
        return f.read().strip()


def _read_mappings(test_name):
    with open(join(DIR, '%s_mappings.txt' % test_name), 'r') as f:
        lines = f.readlines()
    mappings = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        i, o = line.split(',')
        mappings[i] = o
    return mappings


def _read_solution(test_name):
    with open(join(DIR, '%s_out.txt' % test_name), 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main(*sys.argv[1:])
