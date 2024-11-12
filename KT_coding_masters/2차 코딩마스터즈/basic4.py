# 압축된 수열 문제 
def convert_base(num, base): # 진법 변환 

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = chars[num % base] + result
        num //= base
    return result

def calculate_file_size(numbers, base):
    # 각 숫자를 base 진법으로 변환한 길이를 구하고 총합 + (N-1) 만큼의 공백을 더합니다.
    return sum(len(convert_base(num, base)) for num in numbers) + (len(numbers) - 1)

def find_minimum_base(M, numbers):
    # 최소 진법을 투 포인터를 사용해서 탐색 시간복잡도:O(logN)
    left, right = 10, 62
    result = -1

    while left <= right:
        mid = (left + right) // 2
        file_size = calculate_file_size(numbers, mid)
        
        if file_size <= M:
            result = mid
            right = mid - 1  # 더 작은 진법이 가능한지 확인하기 위해 범위를 줄임
        else:
            left = mid + 1  # 더 큰 진법이 필요하므로 범위를 늘림

    return result

# 입력 예시
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 최소 진법 찾기 및 출력
result = find_minimum_base(M, numbers)
print(result)