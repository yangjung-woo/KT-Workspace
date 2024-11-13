# 문제접근 산술연산? < 왜 중급 문제일까?

money = int(input())

# money = x + 0.1*x => 1.1x 
# x = money // (1.1)

x = round(money / 1.1) 

y = x //10 
# 검증: 공급가액 + 부가세가 총액과 같은지 확인
if x + y == money:
    print(x, y)
else:
    print(-1)
