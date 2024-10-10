# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header(' 1. Metric')



st.header('2. Columns')



st.header('3. Dataframe 조회, 수정하기')

# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')

st.markdown('- st.dataframe(상위 15행)')
st.caption('dataframe, write- 10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')


st.markdown('- st.write(상위 15행)')


st.markdown('- st.table(상위 15행)')
st.caption('table- 형태 고정')


st.markdown('- data_editor')
edited_df = 
st.write(edited_df)

# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 3.data.py  또는
# python -m streamlit run 3.data.py