import streamlit as st
import folium
import pandas as pd
# folium 라이브러리 에러가 나는 경우, 아래 방법으로 folium 라이브러리 설치
# File > New > Terminal 선택 후, pip install folium 실행

# 데이터 주소: 'C:/실습파일이 있는 폴더 경로/covid_map.csv' 또는 'covid_map.csv'
map_data = 

# 1. 타이틀과 캡션 표시하기
# 타이틀 : Covid-19 감염현황
# 캡션 : Displaying geographical data on a map using Streamlit and Folium
st.
st.

# 2. checkbox를 이용하여 checkbox 선택여부에 따라
#    write 코드를 사용하여 화면에 데이터프레임 값 나타내기 
if st.
    st.

# # folium.Map(): Folium에서 지도 객체를 생성
# # location: 지도가 초기에 어떤 위치에서 시작할지를 정의 (위도-latitude, 경도-longitude)
# # map_data['lat'].mean()과 map_data['lon'].mean(): 평균 위도와 경도 위치를 지도 중심으로 설정
# # zoom_start: 이 매개변수는 지도의 초기 확대 수준 (default=10, 숫자가 클수록 확대)

# my_map = ( location=[], zoom_start=3 )


# # 지도에 원형 마커와 값 추가
# for                                          # 데이터프레임 한 행 씩 index, row에 담아서 처리 
#                                              # 원 표시 선언
#                                              # 원 중심- 위도, 경도
#                                              # 원의 반지름 /10000
#                                              # 원의 테두리 색상
#                                              # 원을 채움
#                                              # 원의 내부를 채울 때의 투명도
#     ).add_to(my_map)                         # my_map에 원형 마커 추가

#     folium.Marker(                           # 값 표시 선언
#                                              # 값 표시 위치- 위도, 경도
#         icon=folium.DivIcon(html=f"<div>{row['name']} {row['value']:,.0f}</div>") # row['value']:,.0f - 천 단위 구분기호 추가
#     ).add_to(my_map)                          # my_map에 값 추가


# # 지도 그리기
# # st.components.v1.html : Streamlit 라이브러리의 components 모듈에서 html 함수 사용
# # ._repr_html_() : 지도를 HTML 형식으로 표시
# st.components.v1.html(my_map._repr_html_(), width=1000, height=800)


# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 7-3.folium_covid.py  또는
# python -m streamlit run 7-3.folium_covid.py