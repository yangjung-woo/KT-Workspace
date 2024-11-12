def count_ink_usage(start_day, n, holidays):
    # 각 월의 마지막 날
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 요일 인덱스 매핑
    days_of_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    start_idx = days_of_week.index(start_day)
    
    # 색상별 숫자 카운트  빨강 0~9 , .. 
    red_count = [0] * 10
    blue_count = [0] * 10
    black_count = [0] * 10

    holiday_set = set((month, day) for month, day in holidays)
    
    
    for month in range(1, 13):  # 1월부터 12월까지 반복
        for day in range(1, days_in_month[month - 1] + 1):  # 각 월의 날짜 반복
            if start_idx == 0 or (month, day) in holiday_set:
                # 빨간색: 일요일이거나 사용자 지정 공휴일
                for digit in str(day):  # 10일 이면  target_count[0] +=1  ,target_count[1] +=1  
                    red_count[int(digit)] += 1
                
            elif start_idx == 6:
                # 파란색: 토요일
                for digit in str(day):  # 10일 이면  target_count[0] +=1  ,target_count[1] +=1  
                    blue_count[int(digit)] += 1
                
            else:
                # 검은색: 그 외의 요일
                for digit in str(day):  # 10일 이면  target_count[0] +=1  ,target_count[1] +=1  
                    black_count[int(digit)] += 1                
            


            # 다음 날짜로 넘어가면서 요일 업데이트
            start_idx = (start_idx + 1) % 7
    
    # 결과 출력 형식에 맞게 정리
    for i in range(10):
        print(" ".join(map( str,[red_count[i],blue_count[i], black_count[i]])))

start_day = input()
n = int(input())
holidays = []

for _ in range(n):
    holidays.append(list(map(int, input().split())))

count_ink_usage(start_day, n, holidays)