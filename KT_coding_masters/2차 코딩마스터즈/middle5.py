def find_islands(map_string):
    # 1. 기본 섬 개수 계산: 양옆이 'o'인 'g'만 카운트
    initial_islands = count_initial_islands(map_string)
    
    # 2. 최대 섬 개수 계산: 'x'를 적절히 'g'로 변환
    max_islands = calculate_max_islands(map_string)
    
    return initial_islands, max_islands

def count_initial_islands(map_string):
    # 양옆이 'o'로 둘러싸인 'g'만 카운트
    count = 0
    for i in range(1, len(map_string) - 1):
        if map_string[i] == 'g' and map_string[i - 1] == 'o' and map_string[i + 1] == 'o':
            count += 1
    return count

def calculate_max_islands(map_string):
    # 'x'를 'g'로 바꿔 가능한 최대 섬 개수를 계산
    max_islands = 0
    n = len(map_string)
    arr = list(map_string)
    
    # 모든 'x'를 'g'로 변환한 상태에서 섬 개수 계산
    for i in range(n):
        if arr[i] == 'x':
            arr[i] = 'g'
    max_islands = count_total_islands(''.join(arr))
    
    return max_islands

def count_total_islands(map_string):
    # 섬 개수를 계산: 연속된 'g'를 한 섬으로 간주
    count = 0
    in_island = False
    for ch in map_string:
        if ch == 'g':
            if not in_island:
                count += 1
                in_island = True
        else:
            in_island = False
    return count

# 입력
map_string = input()

# 섬 개수 계산
initial_islands, max_islands = find_islands(map_string)

# 결과 출력
print(initial_islands)
print(max_islands)