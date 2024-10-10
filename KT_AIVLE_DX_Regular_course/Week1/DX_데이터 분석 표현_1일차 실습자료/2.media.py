# streamlit 라이브러리 불러오기 
import streamlit as st

st.title('Unit 2. Media elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/media')

st.header('1. Image')
# 이미지 주소: https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80


st.header('2. Audio')
# 오디오 주소: 'C:/실습파일이 있는 폴더 경로/MusicSample.mp3' 또는 'MusicSample.mp3'


st.header('3. Video')
# 비디오 주소: 'C:/실습파일이 있는 폴더 경로/MusicSample.mp3' 또는 'VideoSample.mp4'



# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 2.media.py  또는
# python -m streamlit run 2.media.py