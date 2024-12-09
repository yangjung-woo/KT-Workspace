# 문제접근: 구현 , 자리수는 50을 넘지 않기에 완전탐색으로도 가능함
# 문자열을 앞에서 부터 탐색 3칸씩 끊어서 할 수 없음    ex) 200 720 010 0  < 땡 

# 규칙
# 1. 0으로 끝나는 숫자가 있다면 반드시 앞 2글자는 10이상 알파벳이다 
# >> 문자열을 뒤에서 부터 읽으면 되지 않을까?

encoded = input().strip()
decoded = []

i = len(encoded) -1 # 뒤에서 부터 시작

while i >= 0:
    if encoded[i] =='0':# 0으로 끝나면 반드시 앞 2자리는 10이상 알파벳 
        number  = int(encoded[i -2: i]) # [i-2,i-1]
        decoded.append(chr(ord('a') + number - 1))
        i -= 3
    else: # 1~9사이 알파벳
        number = int(encoded[i])
        decoded.append(chr(ord('a') + number - 1))
        i -=1
        
#print(''.join(decoded))
print(''.join(decoded[::-1]))        



