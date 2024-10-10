# 이 파일은 실습 문제가 아닌 folium map 코딩 이해를 위한 파일로 모든 풀이가 에이블러에게 제공됩니다.

import streamlit as st
import folium
import pandas as pd
# folium 라이브러리 에러가 나는 경우, 아래 방법으로 folium 라이브러리 설치
# File > New > Terminal 선택 후, pip install folium 실행

map_data = pd.DataFrame({
    'lat': [-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'lon': [-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'name': ['Buenos Aires', 'Paris', 'Melbourne', 'St Petersburg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
    'value': [10, 12, 40, 70, 23, 43, 100, 43] 
})

# folium.Map(): Folium에서 지도 객체를 생성
# location: 지도가 초기에 어떤 위치에서 시작할지를 정의 (위도-latitude, 경도-longitude)
# map_data['lat'].mean()과 map_data['lon'].mean(): 평균 위도와 경도 위치를 지도 중심으로 설정
# zoom_start: 이 매개변수는 지도의 초기 확대 수준 (default=10, 숫자가 클수록 확대)

my_map = folium.Map( location=[map_data['lat'].mean(), map_data['lon'].mean()], zoom_start=2 )


# 지도에 원형 마커와 값 추가
for index, row in map_data.iterrows():       # 데이터프레임 한 행 씩 index, row에 담아서 처리 
    folium.CircleMarker(                     # 원 표시 선언
        location=[row['lat'], row['lon']],   # 원 중심- 위도, 경도
        radius=row['value'] / 5,             # 원의 반지름
        color='pink',                        # 원의 테두리 색상
        fill=True,                           # 원을 채움
        fill_opacity=1.0                     # 원의 내부를 채울 때의 투명도
    ).add_to(my_map)                         # my_map에 원형 마커 추가

    folium.Marker(                           # 값 표시 선언
        location=[row['lat'], row['lon']],   # 값 표시 위치- 위도, 경도
        icon=folium.DivIcon(html=f"<div>{row['name']} {row['value']}</div>"), # row['name'], row['value'] 표시
    ).add_to(my_map)                         # my_map에 값 추가

# 타이틀과 캡션 표시하기
st.title('Map with Location Data')
st.caption("Displaying geographical data on a map using Streamlit and Folium")

# 지도 그리기
# st.components.v1.html : Streamlit 라이브러리의 components 모듈에서 html 함수 사용
# ._repr_html_() : 지도를 HTML 형식으로 표시
st.components.v1.html(my_map._repr_html_(), width=800, height=600)


# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 7-2.folium_map.py  또는
# python -m streamlit run 7-2.folium_map.py