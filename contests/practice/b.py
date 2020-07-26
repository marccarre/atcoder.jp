from collections import defaultdict, deque
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
    ordering = defaultdict(set)

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
        # Use BFS to check if ordering can be inferred:
        if c2 in ordering[c1] or run_bfs(c1, c2):
            ordering[c1].add(c2)
            return True
        if c1 in ordering[c2] or run_bfs(c2, c1):
            ordering[c2].add(c1)
            return True
        # Ask for ordering:
        if check_if_less(c1, c2):
            ordering[c1].add(c2)
            return True
        else:
            ordering[c2].add(c1)
            return False

    def run_bfs(c1, c2):
        q = deque([c1])
        visited = set()
        while q:
            u = q.popleft()
            visited.add(u)
            if u == c2:
                return True
            for v in ordering[u]:
                if v not in visited:
                    q.append(v)
        return False

    def check_if_less(c1, c2):
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
