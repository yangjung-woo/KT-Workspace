import requests

# 쿠팡 Open API 인증 정보
API_KEY = 'YOUR_API_KEY'
VENDOR_ID = 'YOUR_VENDOR_ID'

# 발주서 목록 조회 함수
def get_ordersheets(createdAtFrom, createdAtTo, status, maxPerPage=50, nextToken=None):
    # API 엔드포인트
    url = f"https://api-gateway.coupang.com/v2/providers/openapi/apis/api/v4/vendors/{VENDOR_ID}/ordersheets"
    
    # 요청 파라미터
    params = {
        'createdAtFrom': createdAtFrom,
        'createdAtTo': createdAtTo,
        'status': status,
        'maxPerPage': maxPerPage,
        'nextToken': nextToken
    }
    
    # 요청 헤더 (API 인증)
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    # API 호출
    response = requests.get(url, headers=headers, params=params)
    
    # 응답 처리
    if response.status_code == 200:
        return response.json()  # JSON 형태로 응답 반환
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# 발주서 조회
createdAtFrom = "2024-01-01"
createdAtTo = "2024-01-31"
status = "INSTRUCT"  # 예: 발주서 상태

# 첫 번째 페이지 조회
response_data = get_ordersheets(createdAtFrom, createdAtTo, status)

# 응답 데이터 출력
if response_data:
    print("발주서 목록:")
    for order in response_data['data']:
        print(f"Order ID: {order['orderId']}, Status: {order['status']}")
    
    # 페이지가 더 있을 경우 nextToken 사용하여 다음 페이지 조회
    if 'nextToken' in response_data:
        next_token = response_data['nextToken']
        print(f"다음 페이지 토큰: {next_token}")
        # 다음 페이지 데이터 조회
        next_page_data = get_ordersheets(createdAtFrom, createdAtTo, status, nextToken=next_token)
        if next_page_data:
            print("다음 페이지 발주서 목록:")
            for order in next_page_data['data']:
                print(f"Order ID: {order['orderId']}, Status: {order['status']}")
