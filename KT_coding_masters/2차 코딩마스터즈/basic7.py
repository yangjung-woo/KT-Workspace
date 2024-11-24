# 문제접근 : 1. 법인등록번호는 13자리 , 4 2 6 1  < 이중 2자리는 모르는 상황  이를 각각 x,y 로 두고 수식

a = input().strip()
b = input().strip()
c = int(input().strip())

# a와 b를 이어 붙이고 홀수 자리, 짝수 자리각 합을 A, B 에 저장 

strings = ''.join([a,b])
A,B=0,0
for i in range(len(strings)):
    if i%2 ==0: # 홀수번째 수   why? index는 1부터 시작함 
        A += int(strings[i])
    else: # 짝수번째 수
        B += int(strings[i])

#print(A,B)
# 1. 앞 12자리의 홀수 번째 수를 모두 더한 값을 A라고 합니다.
# 2. 앞 12자리의 짝수 번째 수를 모두 더한 값을 B라고 합니다.
# 3. 2 × B + A를 10으로 나눈 나머지를 R이라고 합니다.
# 4. 10 - R이 오류검색번호입니다. 단 10 - R이 10인 경우는 오류검색번호가 0입니다.
# >>  10 - c == R  ==  (2*(B+y) + (A+x)) % 10 이 조건을 만족하는 x, y를 모두 구해보기 

able_list = [] #가능한 모든 법인 종류 리스트 
for x in range(10):
    for y in range(10):
        R = (2*(B+y) + (A+x)) % 10
        
        if 10 - R == 10: # 오류 검색 , 만약 R =10 이면 
            check_error = 0
        
        if check_error == c:
            able_list.append(10*x+y)
#print(able_list)
answer = ['X']*5
for able in able_list:
    if 11<=able<=15: # 상법
        answer[0] = 'O'
    elif 21<=able<=22: # 민법
        answer[1] = 'O'
    elif 31<=able<=51: # 특수
        answer[2] = 'O'
    elif 81<=able<=86: # 외국
        answer[3] = 'O'
    elif able == 71: # 기타
        answer[4] = 'O'


print(''.join(answer))


