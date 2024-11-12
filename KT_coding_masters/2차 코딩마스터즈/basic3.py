# 팬그램은 알파벳의 모든 글자를 사용하여 만든 문장을 말합니다.
# 공백이 없는 문자열이 주어졌을 때, 
# 이 문자열이 팬그램인지 여부를 출력하는 프로그램을 작성해 주세요.

# TheQuickBrownFoxJumpsOverTheLazyDog
# YES




# 문제풀이 : 0 . 팬그램이란? 알파벳 26종이 모두 포함된 문자열
#           1 . 대문자 or 소문자로 통합   // 저는 소문자로 통합했습니다 
#           2 . 중복되지 않도록 저장할 자료구조 //  저는 list에 추가할때 조건을 넣었습니다. 



s = input().lower() # 1 . 대문자 or 소문자로 통합 

alphabet_counter = [] # 카운터용 리스트
for i in s: #  2 . 중복되지 않도록 저장할 자료구조 
    if i not in alphabet_counter:
        alphabet_counter.append(i)


# 중복을 허용하지 않는 자료구조 (ps. 파이썬 기초때 배웠습니다. 이 자료구조는 뭘까요? )
'''
# Set() 자료구조 사용 
alphabet_counter = set()# 카운터용 set 자료구조

for i in s:
    alphabet_counter.add(i)

'''        
 
        

if len(alphabet_counter) ==26:# 알파벳은 총 26개 
    print("YES")
else:
    print("NO")

