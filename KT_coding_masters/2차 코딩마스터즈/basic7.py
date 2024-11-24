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
        if (10 - c)  ==  (2*(B+y) + (A+x))% 10:
            able_list.append(10*x + y )
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


def calculate_check_digit(numbers):
    """
    법인등록번호의 오류검색번호를 계산하는 함수
    """
    # 홀수 위치 숫자 합 계산 (1-based index)
    A = sum(int(numbers[i]) for i in range(0, 12, 2))
    
    # 짝수 위치 숫자 합 계산 (1-based index)
    B = sum(int(numbers[i]) for i in range(1, 12, 2))
    
    # 2 × B + A를 10으로 나눈 나머지 계산
    R = (2 * B + A) % 10
    
    # 10 - R 계산 (10인 경우 0으로 처리)
    check_digit = 10 - R
    if check_digit == 10:
        check_digit = 0
        
    return check_digit

def is_valid_combination(reg_office, corp_type, serial, check_digit):
    """
    주어진 조합이 유효한 법인등록번호인지 확인하는 함수
    """
    # 전체 번호 문자열 생성
    full_number = f"{reg_office}{corp_type}{serial}"
    
    # 계산된 오류검색번호가 주어진 것과 일치하는지 확인
    return calculate_check_digit(full_number) == int(check_digit)

def get_possible_types(reg_office, serial, check_digit):
    """
    가능한 법인 종류를 반환하는 함수
    """
    # 각 법인 종류별 가능한 번호 범위
    type_ranges = {
        'commercial': range(11, 16),  # 상업 법인
        'civil': range(21, 23),       # 민법 법인
        'special': range(31, 52),     # 특수 법인
        'foreign': range(81, 87),     # 외국 법인
        'other': [71]                 # 기타 법인
    }
    
    result = {
        'commercial': False,
        'civil': False,
        'special': False,
        'foreign': False,
        'other': False
    }
    
    # 각 법인 종류별로 가능한 번호를 테스트
    for type_name, number_range in type_ranges.items():
        for num in number_range:
            corp_type = f"{num:02d}"  # 2자리 숫자로 변환
            if is_valid_combination(reg_office, corp_type, serial, check_digit):
                result[type_name] = True
                break
    
    return result

def main():
    # 입력 받기
    reg_office = input().strip()
    serial = input().strip()
    check_digit = input().strip()
    
    # 가능한 법인 종류 확인
    possible_types = get_possible_types(reg_office, serial, check_digit)
    
    # 결과 문자열 생성
    result = ''
    result += 'O' if possible_types['commercial'] else 'X'
    result += 'O' if possible_types['civil'] else 'X'
    result += 'O' if possible_types['special'] else 'X'
    result += 'O' if possible_types['foreign'] else 'X'
    result += 'O' if possible_types['other'] else 'X'
    
    print(result)

if __name__ == "__main__":
    main()