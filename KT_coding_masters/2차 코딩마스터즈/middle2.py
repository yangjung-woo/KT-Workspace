# 문제접근 1. 같은 정수가 서로 떨어져 있을때 , 그 사이 값들은 반드시 외각의 값과 달라야 한다 
# 완전탐색 접근 , 1.숫자들의 등장 위치를 저장할 딕셔너리 생성
#                 2. 각 숫자들에 대해서 조건을 만족하는지 확인  

n = int(input())

nums = list(map(int , input().split()))


def is_good_array(N, a):
    # 숫자 위치를 기록할 딕셔너리
    positions = {}
    
    # 각 숫자의 등장 위치를 기록
    for index, value in enumerate(a):
        if value in positions:
            positions[value].append(index)
        else:
            positions[value] = [index]
    
    # 모든 숫자에 대해 조건을 확인
    for pos in positions.values():
        # 각 숫자는 정확히 두 번 나타나야 함
        if len(pos) != 2:
            return ("NO")
        # 첫 번째와 두 번째 등장 위치
        i, p = pos
        # 중간에 다른 숫자 페어가 겹치는지 확인
        for other_pos in positions.values():
            if other_pos != pos: # 서로 다른 숫자들에 대해서 위치 확인 
                j, q = other_pos
                # 겹치는 페어가 있는지 확인
                if i < j < p < q: #  or j < i < q < p:
                    return ("NO")
    
    return ("YES")

print(is_good_array(n,nums))