# 직각삼각형의 규칙 : 피타고라스 정리 
# 1.a**2 + b**2 = c**2
# 2. 둘레 길이 a +b +c = p(최대 둘레 길이 , p < n)

# 두번째 접근 (피타고라스 수 )
# m과 n을 이용하여 a,b,c 생성. 이때 𝑚과 n은 서로소이고, 𝑚−𝑛은 홀수여야 합니다.
import math
def count_pythagorean_triples(N):
    # 직각삼각형 개수를 기록할 리스트 
    perimeter_count = [0] * (N + 1)
    # 피타고라스 수 생성
    # a = m^2 -n^2
    # b = 2mn
    # c = m^2 +n^2
    # 둘레길이 = a+b+c = 2m*(m+n) , 따라서 m 의 범위는 2~N까지가 아닌  (N/2)**(0.5)까지다  
    for m in range(2, int((N // 2) ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:  # m, n이 서로소이고 m - n이 홀수일 때
                # a, b, c는 피타고라스 수
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                perimeter = a + b + c
                if perimeter > N: # 둘레길이 초과시 종료 
                    break
                # 피타고라스 수의  k 배수들에 대해서도 체크
                k = 1
                while k * perimeter <= N:
                    perimeter_count[k * perimeter] += 1
                    k += 1
    
    # 가장 많은 직각삼각형이 나오는 둘레를 찾기
    max_count = max(perimeter_count)
    for i in range(12, N + 1):
        if perimeter_count[i] == max_count:
            return i, max_count

    return -1, 0  # 해당 조건을 만족하는 것이 없으면

# 입력 처리
N = int(input())
result = count_pythagorean_triples(N)
print(result[0], result[1])



# 첫번째 접근방식 (시간초과 실패 )
# 3중 반복문으로 a, b, c 탐색  
# 단 c = p- a -b 로 계산되므로 a, b만 탐색
# def find_max_triangles(N):
    
#     max_triangle = 0
#     result_perimeter = 0
    
#     for p in range(12,N+1): # 가장 작은 직각삼각형 둘레는 3 4 5 = 12
#         cnt = 0
#         for a in range(1,p//3):
#             for b in range (a , (p-a)//2):
#                 c= p-a-b
#                 if a*a +b*b == c*c:
#                     cnt +=1        
#         if cnt > max_triangle: # 최대길이 직각삼각형 갱신 
#             max_triangle = cnt
#             result_perimeter = p
            
#     return result_perimeter, max_triangle

# N = int(input())
# result = find_max_triangles(N)
# print(result[0], result[1])