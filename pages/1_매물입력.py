"""매물 입력 화면."""
import streamlit as st

import core

st.set_page_config(page_title="매물 입력 - 방값체크", page_icon="🏠")


@st.cache_data
def get_data():
    """매물 데이터를 한 번만 읽어 캐시한다."""
    return core.load_data()


df = get_data()
areas = list(df["area"].unique())
room_types = list(df["room_type"].unique())

st.title("매물 입력")
st.write("보고 계신 매물의 조건을 입력해 주세요. 금액 단위는 모두 만원입니다.")

with st.form("room_form"):
    area = st.selectbox("지역", areas, index=areas.index("와우리") if "와우리" in areas else 0)
    room_type = st.selectbox(
        "방 형태", room_types, index=room_types.index("원룸") if "원룸" in room_types else 0
    )
    size_m2 = st.number_input("면적 (㎡)", min_value=0.0, value=20.0, step=0.5)
    deposit = st.number_input("보증금 (만원)", min_value=0, value=500, step=100)
    monthly_rent = st.number_input("월세 (만원)", min_value=0, value=40, step=1)
    maintenance_fee = st.number_input("관리비 (만원)", min_value=0, value=5, step=1)
    submitted = st.form_submit_button("진단하기")

if submitted:
    room = {
        "area": area,
        "room_type": room_type,
        "size_m2": size_m2,
        "deposit": deposit,
        "monthly_rent": monthly_rent,
        "maintenance_fee": maintenance_fee,
    }
    errors = core.validate_input(room, df)
    if errors:
        for message in errors:
            st.warning(message)
    else:
        st.session_state["room"] = room
        st.success("입력이 저장되었습니다. 진단 결과 화면에서 확인해 주세요.")
        st.page_link("pages/2_진단결과.py", label="진단 결과 보기", icon="📊")
