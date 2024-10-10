import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
# px 모듈이 없다고 에러가 나는 경우에만 아래 방법으로 plotly 라이브러리 설치
# File > New > Terminal 선택 후, 창에 다음 구분 실행 pip install plotly 

st.header('Unit 3. Streamlit Simple chart')

# https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv 읽고 확인하기
chart_data = 
st.

st.subheader('3-1. Simple Line chart')
# use_container_width=True 가로로 화면에 꽉 채워 줌
st.line_chart(chart_data, use_container_width=True) 

st.subheader('3-2. Simple Bar chart')
st.

st.subheader('3-3. Simple area chart')
st.

# st.header('Unit 4. Altair chart') 
# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv 읽고 
# # melt 함수를 사용하여 데이터프레임 unpivot하기
# #### identifier(x)-'date', unpivot column(범례,color)-'teams’, value column(y)-'sales'
# #### id_vars=['date'], var_name='teams', value_name='sales'
# df = 
# df_melted = 

# # columns 함수를 이용하여 좌-원본 데이터, 우-변환 데이터 출력하기
# col1, col2 = 
# with 
#     st.text('원본 데이터')

# with col2:
#     st.text('변경 데이터')


    
# st.subheader('4-1. Altair Line chart')
# chart = alt.Chart(
         
# st.  # use_container_width=True 가로로 화면에 채워 줌


# st.subheader('4-2. Altair Bar chart')

# chart = alt.Chart(
    

# text = alt.Chart(


    
# st.altair_chart(
    
    
# st.subheader('4-3. Altair Scatter chart')

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 확인하기
# iris = 
# st.

# # caption으로 'sepal:꽃받침, petal:꽃잎' 설명 출력하기 


# # petal_length, petal_width로 Altair Circle chart 그리기
# chart = 
    
  
# st.


# st.header('Unit 5. Plotly chart')

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv 읽고 확인하기
# medal = 
# st.

# st.subheader('5-1. Plotly Pie/Donut chart') 
# fig = 
             
# fig.
# fig.
# # fig.update(layout_showlegend=False)  # 범례 표시 제거
# st.

# st.subheader('5-2. Plotly Bar chart')
# # text_auto=True 값 표시 여부
# fig = 
            
# st.

# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 6-2.chart.py  또는
# python -m streamlit run 6-2.chart.py