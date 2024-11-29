# 문제접근 : 규칙? 
# 짐의 위치를 바꾸는것을 10**18번 반복시킴 (짝수번)
# 짐을 짝수번 옮겼을때  R , G  , B 로 맞출수 있으면 정답 

# 즉 세 입력이 R G B 이거나  전부 R G B 가 아니여야 함    


answer = list(input().split())


def all_out(answer):
    if (answer[0] =='R'and answer[1]=='G' and answer[2] =='B')or (answer[0] !='R'and answer[1]!='G' and answer[2] !='B'):
        return True
    else:
        return False
if all_out(answer):
    print('possible')
else:
    print('impossible')