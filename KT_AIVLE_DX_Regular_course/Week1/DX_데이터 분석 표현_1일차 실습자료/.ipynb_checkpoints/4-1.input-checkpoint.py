# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime  

st.title('Unit 4. Input Widgets')
# link_button
st.link_button('Widget Link', 'https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if 


st.header('2. Radio button')
genre = 

if genre == 



st.header('3. Checkbox')     # 😄
agree = 
if 


st.header('4. toggle')
on = 
if 


st.header('5. Select box')
option = st.selectbox('어떻게 연락 드릴까요?',('Email', 'Mobile phone', 'Office phone'))
st.write('네 ', option, ' 잘 알겠습니다')

st.header('6. Multi select')
options = 



# st.header('7. Input: Text/Number')

# st.subheader('**_text_input_**')
# title = 


# st.subheader('**_number_input_**')
# number = 


# st.header('8. Date input')
# ymd = 


# st.header('9. Chat input')
# prompt = 



# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 4-1.input.py  또는
# python -m streamlit run 4-1.input.py