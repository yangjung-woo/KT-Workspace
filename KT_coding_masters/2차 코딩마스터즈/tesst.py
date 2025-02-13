def find_donations(x, y):
    # a: 1000원 후원 인원, b: 5000원 후원 인원, c: 10000원 후원 인원
    for a in range(x + 1):
        for b in range(x + 1 - a):  # a + b가 x를 초과하지 않도록 제한
            c = x - a - b
            if 1000 * a + 5000 * b + 10000 * c == y:
                return {1000: a, 5000: b, 10000: c}
    return None

# 주어진 문제의 입력
x = 11
y = 50000

result = find_donations(x, y)
print(result)