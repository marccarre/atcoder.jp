def main():
    a, b, c, s = inputs()
    abc, s = solution(a, b, c, s)
    print('%d %s' % (abc, s))


def inputs():
    a = int(input())
    b, c = [int(x) for x in input().strip().split()]
    s = input()
    return a, b, c, s


def solution(a, b, c, s):
    return a + b + c, s


if __name__ == '__main__':
    main()
