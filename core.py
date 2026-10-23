"""방값체크 핵심 로직 — streamlit 을 import 하지 않는다 (pytest 로 바로 테스트)."""
from pathlib import Path

import pandas as pd

RATE = 0.06  # 보증금 → 월세 전환율 (연 6%)
DATA_PATH = Path(__file__).parent / "data" / "rooms.csv"


def load_data(path=DATA_PATH):
    """매물 CSV 를 읽어 DataFrame 으로 돌려준다. 열 목록은 data/README.md 참고."""
    return pd.read_csv(path)


# US-3 에서 아래 함수를 SPEC.md "2. 계산 규칙" 대로 추가한다.
# validate_input(room) / monthly_cost(deposit, rent, fee) / find_similar(df, area, room_type, size_m2) / judge(my_cost, similar)
