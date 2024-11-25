def get_min_max_islands(world_map):
    n = len(world_map)
    min_islands = 0
    max_islands = 0

    # 최소 섬 계산: 모든 'x'를 바다('o')로 간주
    min_world = world_map.replace('x', 'o')
    min_islands = sum(1 for segment in min_world.split('o') if 'g' in segment)

    # 최대 섬 계산: 모든 'x'를 땅('g')으로 간주
    max_islands = 0
    is_land = False

    for char in world_map:
        if char in ['g', 'x']:  # 땅일 가능성이 있는 경우
            if not is_land:
                max_islands += 1
                is_land = True
        elif char == 'o':  # 바다를 만나면
            is_land = False

    return min_islands, max_islands

# 입력 받기
world_map = input().strip()

# 결과 계산 및 출력
min_val, max_val = get_min_max_islands(world_map)
print(f"{min_val} {max_val}")