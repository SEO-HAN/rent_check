"""진단 결과 화면."""
import pandas as pd
import streamlit as st

import core

st.set_page_config(page_title="진단 결과 - 방값체크", page_icon="🏠")


@st.cache_data
def get_data():
    """매물 데이터를 한 번만 읽어 캐시한다."""
    return core.load_data()


st.title("진단 결과")
st.caption("※ 수업용 가상 매물 120건을 기준으로 한 진단입니다. 실제 시세와 다를 수 있습니다.")

room = st.session_state.get("room")
if not room:
    st.warning("먼저 매물 입력 화면에서 진단해 주세요")
    st.page_link("pages/1_매물입력.py", label="매물 입력하러 가기", icon="✏️")
    st.stop()

df = get_data()
similar = core.find_similar(df, room["area"], room["room_type"], room["size_m2"])
if similar.empty:
    st.warning("비슷한 매물을 찾지 못했습니다. 다른 조건으로 입력해 주세요")
    st.page_link("pages/1_매물입력.py", label="매물 다시 입력하기", icon="✏️")
    st.stop()

my_cost = core.monthly_cost(room["deposit"], room["monthly_rent"], room["maintenance_fee"])
result = core.judge(my_cost, similar)

st.caption(
    f"{room['area']} · {room['room_type']} · {room['size_m2']:g}㎡ · "
    f"보증금 {room['deposit']:g}만원 · 월세 {room['monthly_rent']:g}만원 · 관리비 {room['maintenance_fee']:g}만원"
)

col1, col2 = st.columns(2)
col1.metric(
    "내 환산 월 비용",
    f"{my_cost:g}만원",
    delta=f"{result['diff_pct']:+.1f}%",
    delta_color="inverse",
)
col2.metric("적정 월 비용 (비슷한 매물 중앙값)", f"{result['fair_cost']:g}만원")

verdict = result["verdict"]
if verdict == "비쌈":
    st.error("이 매물은 시세보다 **비싼 편**입니다.")
elif verdict == "저렴":
    st.success("이 매물은 시세보다 **저렴한 편**입니다.")
else:
    st.info("이 매물은 시세와 비슷한 **적정 수준**입니다.")

st.subheader("판정 근거")
for reason in result["reasons"]:
    st.write(f"- {reason}")

st.subheader("환산 월 비용 비교")
chart_df = similar[["room_id", "monthly_cost"]].copy()
chart_df["구분"] = "비교 매물"
chart_df = pd.concat(
    [chart_df, pd.DataFrame({"room_id": ["내 매물"], "monthly_cost": [my_cost], "구분": ["내 매물"]})],
    ignore_index=True,
)
st.bar_chart(
    chart_df,
    x="room_id",
    y="monthly_cost",
    color="구분",
    x_label="매물",
    y_label="환산 월 비용 (만원)",
    sort="monthly_cost",
)
st.caption(f"'내 매물' 막대를 비교 매물과 견주어 보세요. 적정 월 비용(중앙값)은 {result['fair_cost']:g}만원입니다.")

st.subheader(f"비교한 매물 {len(similar)}건")
st.dataframe(
    similar[
        ["room_id", "area", "room_type", "size_m2", "deposit", "monthly_rent",
         "maintenance_fee", "monthly_cost"]
    ],
    hide_index=True,
    width="stretch",
    column_config={
        "room_id": "매물 번호",
        "area": "지역",
        "room_type": "방 형태",
        "size_m2": "면적(㎡)",
        "deposit": "보증금(만원)",
        "monthly_rent": "월세(만원)",
        "maintenance_fee": "관리비(만원)",
        "monthly_cost": "환산 월 비용(만원)",
    },
)
st.caption("비교 데이터는 수업용 가상 매물이며 실제 시세와 다를 수 있습니다.")
