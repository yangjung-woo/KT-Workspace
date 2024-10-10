# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')

# Heading & Body - header, subheader, text, caption
st.markdown('### Heading & Body - title, header, subheader, text')


# Heading & Body - markdown
st.markdown('### Heading & Body - markdown')


# FORMATTED TEXT - divider, caption
st.markdown('### divider')

st.markdown('### Caption')


# FORMATTED TEXT - Latex & Code
# a + ar + ar^2 + ar^3
st.markdown('### Code & Latex')


# write
# String, data_frame, chart, graph, LaTex 등의 objects 출력
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})


# 파일실행 방법
# 메뉴 탭 선택: File > New > Terminal(anaconda prompt)
# streamlit run 1.text.py  또는
# python -m streamlit run 1.text.py