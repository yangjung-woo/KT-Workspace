
# 문제설명
# X미터 떨어진 철로에 양쪽 끝에 두 대의 기차가 시속 Y킬로미터의 속도로 서로를 향해 출발했습니다.
# 이 기차 사이에는 시속 Z킬로미터의 속도로 기차 사이를 왔다 갔다 하는 파리가 한 마리 있는데, 둘 중 한 기차의 방향으로 날다가 기차와 부딪히면 즉시 반대 방향으로 날기 시작합니다.
# 두 기차가 충돌할 때까지 파리가 이동한 거리를 출력하는 프로그램을 작성해 주세요.
X , Y , Z = map(int, input().split())
time = X / (2*Y)
# 충돌까지 걸리는 시간 
# 파리가 기차랑 박치기하고 방향전환 하는데 대기시간도 없고 속력이 유지됨
# 즉 충돌 횟수와 상관 없이 충돌까지 걸리는 시간 * 파리의 속력 = 파리가 이동한 거리
print(int(Z*time))