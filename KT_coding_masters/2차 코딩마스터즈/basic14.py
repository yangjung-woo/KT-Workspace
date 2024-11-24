# 묵찌빠 봇 

#문제 접근 
#1. 공수 결정 
#2. 리스트 순환(묵 찌 빠  ,승패 결정까지)   > 최대 반복횟수를 정해야 함
#  > 두 리스트 개수의 최소공배수 만큼만 반복하면 그 이후로는 무한루프 


# 1. 가위바위보 승자를 결정할 함수를 만들면 편할듯?  (공수결정 마다 필요함 )

def winner(hand1,hand2):
    # 1: 가위, 2: 바위, 3: 보
    # 비기면 0, bot1이 이기면 1, bot2가 이기면 2 반환
    if hand1 == hand2:
        return 0
    elif (hand1 == 1 and hand2 == 3) or (hand1 == 2 and hand2 == 1) or (hand1 == 3 and hand2 == 2):
        return 1
    else:
        return 2

N, M = map(int, input().split())
moves1 = list(map(int, input().split()))
moves2 = list(map(int, input().split()))


turn_cnt = 0

# 최대 반복 루프 수 
max_turn = len(moves1)* len(moves2)

while True:# 가위바위보 (공수 결정)
    hand1 = moves1[turn_cnt % len(moves1)]
    hand2 = moves2[turn_cnt % len(moves2)]
    
    result = winner(hand1, hand2)
    if result != 0: # 공수가 결정되면 탈출 
        attak = result
        break
    
    turn_cnt +=1
    
    if turn_cnt>= max_turn: # 영원히 비기는 경우 게임 종료 
        print(0)
        exit(0)


while True:
    turn_cnt+=1
    hand1 = moves1[turn_cnt % len(moves1)]
    hand2 = moves2[turn_cnt % len(moves2)]
    
    if attak ==1:   # hand1이 공격 
        
        if hand1 == hand2: # hand1의 승리 
            print(1)
            exit(0)
        
        if winner(hand1,hand2) ==2: # 공수교대 
            attak = 2
        
    else :# hand2이 공격 
        if hand1 == hand2: # hand1의 승리 
            print(2)
            exit(0)
        
        if winner(hand1,hand2) ==1: # 공수교대 
            attak = 1
    
    if turn_cnt>= max_turn: # 영원히 비기는 경우 게임 종료 
        print(0)
        exit(0)
