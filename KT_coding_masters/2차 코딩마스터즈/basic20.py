before = list(input().strip())
after = list(input().strip())

before.sort()
after.sort()


if before == after:
    print('YES')

else:
    print('NO')
    