import streamlit as st
import pandas as pd

# 메인페이지 
# Iris 사진 나타내기- https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 나타내기 
def main_page():
    st.header('Main Page')

    iris = 


# 2페이지: 세 개의 columns으로 나누어 꽃 이름과 사진 나타내기
def page2():
    st.header('Page 2')


        st.text('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg')

        st.text('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg')

        st.text('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg')

# 3페이지: 세 개의 tab을 사용하여 iris 3가지 꽃 나타내기 (width=500)
def page3():
    st.header('Page 3')


        st.header('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg', width=500)       

        st.header('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg', width=500)      

        st.header('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg', width=500)   

# 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }
page_names_to_funcs = 

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = 

# 해당 페이지 부르기
page_names_to_funcs[

# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 5-3.layouts.py  또는
# python -m streamlit run 5-3.layouts.py