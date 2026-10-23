"""방값체크 핵심 로직 — streamlit 을 import 하지 않는다 (pytest 로 바로 테스트)."""
from pathlib import Path

import pandas as pd

RATE = 0.06  # 보증금 → 월세 전환율 (연 6%)
DATA_PATH = Path(__file__).parent / "data" / "rooms.csv"


def load_data(path=DATA_PATH):
    """매물 CSV 를 읽어 DataFrame 으로 돌려준다. 열 목록은 data/README.md 참고."""
    return pd.read_csv(path)


def validate_input(room, df=None):
    """입력 dict 를 검사해 오류 메시지 목록을 돌려준다. 문제가 없으면 빈 리스트다.

    room 의 키: area, room_type, size_m2, deposit, monthly_rent, maintenance_fee
    """
    if df is None:
        df = load_data()
    errors = []

    if room.get("area") not in set(df["area"]):
        errors.append("지역은 목록에 있는 값 중에서 골라 주세요")
    if room.get("room_type") not in set(df["room_type"]):
        errors.append("방 형태는 목록에 있는 값 중에서 골라 주세요")

    checks = [
        ("size_m2", 5, 100, "면적은 5㎡ 이상 100㎡ 이하로 입력해 주세요"),
        ("deposit", 0, 10000, "보증금은 0만원 이상 10000만원 이하로 입력해 주세요"),
        ("monthly_rent", 1, 300, "월세는 1만원 이상 300만원 이하로 입력해 주세요"),
        ("maintenance_fee", 0, 50, "관리비는 0만원 이상 50만원 이하로 입력해 주세요"),
    ]
    for key, low, high, message in checks:
        value = room.get(key)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not low <= value <= high:
            errors.append(message)
    return errors


def monthly_cost(deposit, rent, fee):
    """환산 월 비용(만원)을 소수 첫째 자리까지 계산한다: 월세 + 관리비 + 보증금 × RATE / 12."""
    return round(rent + fee + deposit * RATE / 12, 1)


def find_similar(df, area, room_type, size_m2):
    """같은 지역·방 형태에 면적 차이 ±5㎡ 이내인 매물을 찾아 monthly_cost 열을 붙여 돌려준다.

    3건 미만이면 면적 조건을 빼고 같은 지역·방 형태 전체를 돌려준다.
    """
    same = df[(df["area"] == area) & (df["room_type"] == room_type)].copy()
    similar = same[(same["size_m2"] - size_m2).abs().round(6) <= 5]
    if len(similar) < 3:
        similar = same
    similar = similar.copy()
    similar["monthly_cost"] = [
        monthly_cost(d, r, f)
        for d, r, f in zip(similar["deposit"], similar["monthly_rent"], similar["maintenance_fee"])
    ]
    return similar


def judge(my_cost, similar):
    """내 환산 월 비용을 비슷한 매물과 비교해 판정 결과 dict 를 돌려준다.

    fair_cost(중앙값), diff_pct(차이율 %), verdict(비쌈/적정/저렴), reasons(근거 문장 3개)
    """
    fair_cost = float(similar["monthly_cost"].median())
    diff_pct = round((my_cost - fair_cost) / fair_cost * 100, 1)
    if diff_pct >= 10:
        verdict = "비쌈"
    elif diff_pct <= -10:
        verdict = "저렴"
    else:
        verdict = "적정"

    low = float(similar["monthly_cost"].min())
    high = float(similar["monthly_cost"].max())
    reasons = [
        f"비슷한 매물 {len(similar)}건의 환산 월 비용 중앙값은 {fair_cost:g}만원입니다.",
        f"내 매물의 환산 월 비용은 {my_cost:g}만원으로, 적정 비용보다 {diff_pct:+.1f}% 차이가 납니다.",
        f"비슷한 매물의 환산 월 비용 범위는 {low:g}~{high:g}만원이며, 판정은 '{verdict}'입니다.",
    ]
    return {"fair_cost": fair_cost, "diff_pct": diff_pct, "verdict": verdict, "reasons": reasons}
