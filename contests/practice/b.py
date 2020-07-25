from functools import lru_cache
import sys


def main():
    n, q = inputs()
    array = solution(n, q)
    print('! %s' % array, flush=True)


def inputs():
    n, q = [int(x) for x in input().strip().split()]
    return n, q


def solution(n, _):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    array = [chars[i] for i in range(n)]

    def merge_sort(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if less(left[l], right[r]):
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        if l < len(left):
            merged.extend(left[l:])
        if r < len(right):
            merged.extend(right[r:])
        return merged

    @lru_cache()
    def less(c1, c2):
        print('? %s %s' % (c1, c2), flush=True)
        resp = input().strip()
        if resp == '<':
            return True
        elif resp == '>':
            return False
        else:
            print('INVALID RESPONSE: [%s]' % resp, flush=True)
            sys.exit(1)

    return ''.join(merge_sort(array))


if __name__ == '__main__':
    main()
