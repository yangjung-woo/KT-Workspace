# 문제접근: 규칙?
# x(상승일) + y(하락일) = N 이라 할때 (단, x , y 는 정수)

# 100x - 100y = K 인 경우의 수들을 구해라 (x,y)
# x - y = K /100 ...(1)
# x + y = N   ...(2)
# 2x =  N + K/100

# x = (N + K/100)/2   << 정수여야고  0<=x<=N을 만족해야함 

# 총 N 일중에서 x 일만 상승하는 경우의 수 구하기  == 조합 
# 조합 C(N,x)


# from math import comb # 조합의 수 계산 라이브러리

def stock_profit_cases(N, K):

    k = K // 100
    x = (N + k) / 2
    
    # comb 라이브러리를 못 쓰는 경우 
    if x.is_integer() and 0 <= x <= N:
        
        mul = 1
        div = 1
        for i in range(int(x)):
            mul = mul * (N-i)
            div = div *(i+1)
        
        return(mul//div)
    return 0
    
    
    # # x가 정수인지 확인하고, 0 <= x <= N 조건 만족
    # if x.is_integer() and 0 <= x <= N:
    #     return comb(N, int(x))
    # return 0

N, K = map(int, input().split())
print(stock_profit_cases(N, K))