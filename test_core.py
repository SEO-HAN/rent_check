"""core.py 테스트 — python -m pytest -q 로 실행한다."""
import core


def test_load_data_columns():
    """데이터가 120건이고 data/README.md 의 11개 열이 그대로 있는지 확인한다."""
    df = core.load_data()
    assert len(df) == 120
    assert list(df.columns) == [
        "room_id", "area", "room_type", "size_m2", "floor", "building_age",
        "walk_min", "deposit", "monthly_rent", "maintenance_fee", "full_option",
    ]


# US-3 에서 SPEC.md "검증용 기대값" 5개와 예외 입력 테스트를 추가한다.
