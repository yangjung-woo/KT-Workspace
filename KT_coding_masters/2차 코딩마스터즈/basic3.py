

# 팬그램은 알파벳의 모든 글자를 사용하여 만든 문장을 말합니다.
# 공백이 없는 문자열이 주어졌을 때, 
# 이 문자열이 팬그램인지 여부를 출력하는 프로그램을 작성해 주세요.

# TheQuickBrownFoxJumpsOverTheLazyDog
# YES

s = input().lower()
s2= list(s.strip())

alphabet_counter = []# 카운터용 리스트 
for i in s:
    if i not in alphabet_counter:
        alphabet_counter.append(i)

if len(alphabet_counter) ==26:# 알파벳은 총 26개 
    print("YES")
else:
    print("NO")



# 또 다른 방식 set 자료구조 사용 
alphabet_counter = set()# 카운터용 set 자자료구조

for i in s:
    alphabet_counter.add(i)

if len(alphabet_counter) ==26:# 알파벳은 총 26개 
    print("YES")
else:
    print("NO")