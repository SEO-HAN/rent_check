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
st.caption(f"비교 데이터: 수업용 가상 데이터, 매물 {len(df)}건 (실제 시세와 다를 수 있습니다)")

st.page_link("pages/1_매물입력.py", label="진단 시작", icon="▶️")

st.subheader("지역·방 형태별 시세 요약")
summary = core.area_summary(df)
if summary.empty:
    st.warning("시세 요약을 만들 데이터가 없습니다")
else:
    st.dataframe(
        summary,
        hide_index=True,
        width="stretch",
        column_config={
            "area": "지역",
            "room_type": "방 형태",
            "count": "매물 수(건)",
            "monthly_rent": "월세 중앙값(만원)",
            "monthly_cost": st.column_config.NumberColumn("환산 월 비용 중앙값(만원)", format="%.2f"),
        },
    )
    st.caption("환산 월 비용 = 월세 + 관리비 + 보증금 × 0.06 / 12. 수업용 가상 데이터 기준입니다.")
