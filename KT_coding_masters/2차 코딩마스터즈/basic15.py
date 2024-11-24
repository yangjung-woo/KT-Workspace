# 입력 및 출력 예제
code = input().strip()

r = int(code[1:3], 16) # 16진수를 가져와 10진수로 변환 
g = int(code[3:5], 16)
b = int(code[5:7], 16)
    
# 평균 계산 후 반올림
gray = round((r + g + b) / 3)
    
# 회색조 값으로 헥스 코드 생성
gray_hex = f'#{gray:02X}{gray:02X}{gray:02X}'  # 2자리 X(16진수)로 변환 

print(gray_hex)