# 문제 접근: Trailing Zero의 개수는 팩토리얼 값에서 끝에 있는 0의 개수
# > 2 x 5 할때 마다 0이 하나씩 생김, 팩토리얼에선 2 보다 5가 더 적게 등장하므로 
#   10의 개수 = min(2의 등장 , 5의 등장)   >> 소인수 분해 5의 개수가 Trailing Zero를 정함 
# (keypoint) 1. 탐색 범위는  이진 탐색을 이용  0 ~ 5*n 중에서 mid = (0 +5*n )//2
#            2. mid! 의 소인수들 중에서  5의 개수를 비교해서 탐색범위 좁히기 



def count_5_in_factorial(k): # 소인수 분해 5의 개수 구하기 
    count = 0
    power_of_five = 5
    while power_of_five <= k:
        count += k // power_of_five
        power_of_five *= 5
    return count

def find_minimum_factorial(n):
    # 이진 탐색으로 최소 k 찾기 >  완전탐색 시간복잡도 O(n * logn) , 이진탐색시 시간복잡도(logn * logn)
    low, high = 0, 5 * n
    result = high
    while low <= high:
        mid = (low + high) // 2
        if count_5_in_factorial(mid) >= n:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

# 입력 및 출력 처리
n = int(input())
print(find_minimum_factorial(n))