import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

st.title('종합 실습')
st.header('_2021 서울교통공사 지하철 월별 하차 인원_')

#  data_subway_in_seoul.csv
#  encoding='cp949'  읽어오고 확인하기 
df = 

#  button을 누르면 원본데이터 주소가 나타남: https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do
if st.  ('data copyright link'):
    st.write(   )

#  checkbox를 선택하면 원본 데이터프레임이 나타남
if st.  ('원본 데이터 보기'):
    st.subheader('1. 원본 데이터- df')
    st.

# '구분' 컬럼이 '하차'인 데이터를 선택
# 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_off = 
if st.checkbox('하차 데이터 보기'):
    st.subheader('2. 하차 데이터- df_off')
    st.

# 불필요한 컬럼 '날짜','연번','역번호','역명','구분','합계' 제외
# 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_line = df_off.
if st.checkbox('호선, 시간대별 인원수 보기'):
    st.subheader('3. 호선, 시간대별 인원수- df_line')
    st.

#  melt 함수 사용 unpivot: identifier-'호선', unpivot column-'시간', value column-'인원수' 
# 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_line_melted = pd.melt(df_line, 
if st.checkbox('Unpivot 데이터 보기'):
    st.subheader('4. 구조변경 (Unpivot by melt) 데이터- df_line_melted')
    st.

# '호선','시간' 별 '인원수' 합,  as_index=False 저장 & 확인 
# 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_line_groupby = df_line_melted.
if st.checkbox('호선, 시간대별 인원 집계 데이터 보기'):
    st.subheader('5. 호선, 시간대별 인원 집계 데이터- df_line_groupby')
    st.

# altair mark_line 차트 그리기
st.subheader('전체 호선 시간대별 하차 인원 (5.df_line_groupby)')

# 데이터프레임- df_line_groupby
# x- '시간', y- '인원수', color- '호선', strokeDash- '호선'
chart = alt.Chart(df_line_groupby).    .encode(
         x=       ).properties(width=650, height=350)
st.altair_chart(chart, use_container_width=True)


st.subheader('선택한 호선의 시간대별 하차 인원')

# selectbox를 사용하여 '호선' 선택
# 데이터프레임- df_line_groupby  ('호선', '시간대별' 인원 집계 )
# ['호선'] 컬럼에 대해 .unique() 매소드를 사용하여 
# selectbox에 호선이 각각 하나만 나타나게 함
option =  st.    ('호선 선택 (5.df_line_groupby)',df_line_groupby['호선'].    )

# .loc 함수를 사용하여 선택한 호선 데이터 선별하고
# 새로운 데이터 프레임-에 저장 & 확인 
df_selected_line = df_line_groupby.   [df_line_groupby['호선'] ==   ]
st.write(option, ' 데이터 (df_selected_line)', df_selected_line)

# altair mark_area 차트 그리기
# 데이터프레임- df_selected_line, x- '시간', y- '인원수'
chart = alt.Chart(df_selected_line).   ().encode(
         x=       ).properties(width=650, height=350)
st.altair_chart(chart, use_container_width=True)


st.subheader('선택한 역의 시간대별 하차 인원')

# selectbox를 사용하여 '하차역' 선택
# ['역명'] 컬럼에 대해  .unique() 매소드를 사용하여 
# selectbox에 역명이 각각 하나만 나타나게 함

option = st.selectbox('하차역 선택 (2.df_off)', df_off['역명'].    )

# .loc 함수를 사용하여 선택한 역의 데이터를 선별하고
# 새로운 데이터 프레임에 저장
df_sta = df_off.   [df_off['역명'] ==      ]
st.write(option, '하차 데이터 (df_sta)', df_sta)

# 불필요한 컬럼 '연번','호선','역번호','역명','구분','합계' 제외하고 기존 데이터 프레임에 저장
# 참고) df_sta_drop = df_sta[df_sta.columns.difference(['연번', '호선', '역번호', '역명','구분','합계'])]
df_sta_drop = df_sta.    (['연번', '호선', '역번호', '역명','구분','합계'],      )
st.write('날짜, 시간대별 인원수 (df_sta_drop)', df_sta_drop)

# melt 함수 사용 unpivot: identifier-'날짜', unpivot column-'시간', value column-'인원수' 
# 새로운 데이터 프레임-에 저장 & 확인
df_sta_melted = pd.    (df_sta_drop,           )
st.write('Unpivot (df_sta_melted)', df_sta_melted)

# '시간' 별 '인원수' 집계 , as_index=False
# 새로운 데이터 프레임-에 저장 & 확인
df_sta_groupby = df_sta_melted.
st.write(option, ' 집계 데이터 (df_sta_groupby)', df_sta_groupby)

# altair mark_bar  chart + text 그리기
# 데이터프레임- df_sta_groupby,  x-'시간',  y-'인원수'
chart = alt.Chart(df_sta_groupby).    .encode(
         x=           ).properties(width=650, height=350)
text = alt.Chart(df_sta_groupby).mark_text(dx=0, dy=-10, color='black').encode(
    x='시간', y='인원수', text=alt.Text('인원수:Q', format=',.0f') ) 
# format=',.0f' : 천 단위 구분기호+소수점 이하 0

st.altair_chart(        , use_container_width=True)

# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 8.prac.py  또는
# python -m streamlit run 8.prac.py