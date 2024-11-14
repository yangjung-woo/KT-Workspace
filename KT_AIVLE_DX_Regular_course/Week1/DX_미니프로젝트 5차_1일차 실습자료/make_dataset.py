# 함수 만들기(수정 필요)
def make_dataset(store_id, product_id):
    # 데이터 준비
    leadtime = products.loc[products['product_id']==product_id, 'leadtime'].values[0]
    temp1 = sales.loc[(sales['store_id']==store_id) & (sales['product_id']==product_id), ['date', 'qty']]
    temp2 = orders.loc[orders['store_id']==store_id, ['date', 'count']]
    temp3 = pd.merge(temp1, temp2, on='date', how='left')
 
    # 매장별 지역 정보 병합
    # store_info = stores[['store_id', 'city', 'state']]
    # temp3 = pd.merge(temp3, store_info[store_info['store_id'] == store_id], on='store_id', how='left')
 
    
    # 날짜 요소 추출
    temp3['weekday'] = temp3['date'].dt.day_name()
    temp3['month'] = temp3['date'].dt.month
    # 추가 (요일별 평균)
    temp3['weekday_avg_qty'] = temp3.groupby('weekday')['qty'].transform('mean')
 
    # Oil Price
    temp3 = pd.merge(temp3, oil_price, on='date', how='left')
    temp3['wti_price'] = temp3['wti_price'].rolling(14, min_periods=1).mean()
 
 
    # **새로운 변수 추가** (lagged 변수)
    temp3['qty_lag_1'] = temp3['qty'].shift(1)  # 1일 전 판매량
    temp3['qty_lag_7_mean'] = temp3['qty'].rolling(7, min_periods=1).mean().shift(1)  # 최근 7일 평균 판매량 (shift to prevent leakage)
 
    # 주간 누적 판매량 (추가)
    temp3['weekly_qty_sum'] = temp3['qty'].rolling(7, min_periods=1).sum()
 
    # 계절성 변수(추가)
    temp3['season'] = temp3['month'].apply(lambda x: 'winter' if x in [12, 1, 2] 
                                       else 'spring' if x in [3, 4, 5]
                                       else 'summer' if x in [6, 7, 8]
                                       else 'fall')
 
    # 계절 원-핫 인코딩
    temp3 = pd.get_dummies(temp3, columns=['season'], drop_first=True, dtype=int)
 
 
    # # 지역별 판매 패턴
    # temp3['state_avg_qty'] = temp3.groupby('state')['qty'].transform('mean')
    # temp3['city_avg_qty'] = temp3.groupby('city')['qty'].transform('mean')
 
    
    # Target 추가
    temp3['target'] = temp3['qty'].shift(-leadtime)
 
    # 결측치 처리
    temp3.interpolate(method='linear', inplace=True)
    temp3.fillna(method='bfill', inplace=True)
 
    # 결과 반환
    return temp3