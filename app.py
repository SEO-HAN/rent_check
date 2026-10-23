"""방값체크 홈 화면."""
import streamlit as st

import core

st.set_page_config(page_title="방값체크", page_icon="🏠")


@st.cache_data
def get_data():
    """매물 데이터를 한 번만 읽어 캐시한다."""
    return core.load_data()


df = get_data()

st.title("🏠 방값체크")
st.subheader("수원대 주변 자취방 월세 적정가 진단")
st.write("자취방을 구하는 대학생을 위해, 매물 조건을 넣으면 비슷한 매물 시세와 비교해 적정 월세와 판정 근거를 알려 드립니다.")
st.caption(f"비교 데이터: 수업용 가상 매물 {len(df)}건 (실제 시세와 다를 수 있습니다)")

st.page_link("pages/1_매물입력.py", label="진단 시작", icon="▶️")
