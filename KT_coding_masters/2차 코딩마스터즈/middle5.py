def get_min_max_islands(world_map):
    n = len(world_map)
    min_islands = 0
    max_islands = 0
    
    # 현재 확인된 섬의 개수 (x가 아닌 부분에서의 섬)
    current_islands = 0
    
    # 연속된 땅 여부
    is_land = False
    
    # x의 연속된 그룹을 찾아서 처리
    i = 0
    while i < n:
        if world_map[i] == 'x':
            # x의 연속된 부분 찾기
            x_start = i
            while i < n and world_map[i] == 'x':
                i += 1
            x_end = i - 1
            
            # x 그룹 앞뒤의 문자 확인
            left_char = world_map[x_start - 1] if x_start > 0 else 'o'
            right_char = world_map[x_end + 1] if x_end < n - 1 else 'o'
            
            # 최대값 계산을 위한 x 그룹 처리
            if x_end - x_start + 1 >= 2:  # x가 2개 이상이면
                if left_char == 'o' and right_char == 'o':
                    max_islands += 2  # 최대 2개의 섬 생성 가능
                elif left_char == 'o' or right_char == 'o':
                    max_islands += 1  # 최대 1개의 섬 생성 가능
            else:  # x가 1개면
                if left_char == 'o' and right_char == 'o':
                    max_islands += 1  # 최대 1개의 섬 생성 가능
        else:
            # x가 아닌 현재 위치 처리
            if world_map[i] == 'g':
                if not is_land:
                    is_land = True
            else:  # 'o'
                if is_land:
                    current_islands += 1
                    is_land = False
            i += 1
    
    # 현재까지 확인된 섬의 개수를 최소값으로
    min_islands = current_islands
    max_islands += current_islands
    
    return min_islands, max_islands

# 입력 받기
world_map = input().strip()

# 결과 계산 및 출력
min_val, max_val = get_min_max_islands(world_map)
print(f"{min_val} {max_val}")


