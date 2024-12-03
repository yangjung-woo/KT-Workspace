# 사원수 곱셈 프로그램
# 문제접근: 구현: 수식을 작성해보자 

# 첫 번째 사원수: a + bi + cj + dk
# 두 번째 사원수: w + xi + yj + zk
    

def multiply_quaternions(a, b, c, d, w, x, y, z):

    # 결과 계산
    o = a * w - b * x - c * y - d * z
    p = a * x + b * w + c * z - d * y
    q = a * y - b * z + c * w + d * x
    r = a * z + b * y - c * x + d * w

    return o, p, q, r


a, b, c, d = map(int, input().split())
w, x, y, z = map(int, input().split())


o, p, q, r = multiply_quaternions(a, b, c, d, w, x, y, z)
print(o, p, q, r)