

tel = input()


def check_valid_tel(tel):
    # 길이와 시작 문자열 확인
    if len(tel) != 13 or not tel.startswith("010-"): # 13길이 , 010-으로 시작하지 않으면 종료
        return "invalid"
    
    # 전화번호 분리 및 형식 확인
    parts = tel.split('-')
    if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
        if len(parts[1]) == 4 and len(parts[2]) == 4:
            return "valid"
            
    
    return "invalid"

print(check_valid_tel(tel))