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


import pytest

# (지역, 방 형태, 면적, 보증금, 월세, 관리비, 내 비용, 비교 매물 수, 적정가, 차이율, 판정)
EXPECTED = [
    ("와우리", "원룸", 20, 500, 40, 5, 47.5, 10, 38.5, 23.4, "비쌈"),
    ("와우리", "원룸", 20, 500, 30, 5, 37.5, 10, 38.5, -2.6, "적정"),
    ("수원역", "1.5룸", 28, 500, 40, 5, 47.5, 10, 54.25, -12.4, "저렴"),
    ("병점역", "투룸", 40, 1000, 45, 7, 57.0, 8, 59.0, -3.4, "적정"),
    ("봉담읍내", "원룸", 60, 500, 30, 5, 37.5, 10, 33.75, 11.1, "비쌈"),
]


@pytest.mark.parametrize(
    "area, room_type, size, deposit, rent, fee, cost, count, fair, diff, verdict", EXPECTED
)
def test_expected_values(area, room_type, size, deposit, rent, fee, cost, count, fair, diff, verdict):
    """SPEC.md 검증용 기대값 5건과 계산 결과가 일치하는지 확인한다."""
    my_cost = core.monthly_cost(deposit, rent, fee)
    assert my_cost == cost
    similar = core.find_similar(core.load_data(), area, room_type, size)
    assert len(similar) == count
    result = core.judge(my_cost, similar)
    assert result["fair_cost"] == pytest.approx(fair)
    assert result["diff_pct"] == pytest.approx(diff)
    assert result["verdict"] == verdict
    assert len(result["reasons"]) == 3


def _room(**changes):
    """기본 입력(와우리 / 원룸 / 20 / 500 / 40 / 5)에 일부 값만 바꾼 dict 를 만든다."""
    room = {"area": "와우리", "room_type": "원룸", "size_m2": 20, "deposit": 500,
            "monthly_rent": 40, "maintenance_fee": 5}
    room.update(changes)
    return room


def test_validate_ok():
    """정상 입력은 오류가 없다."""
    assert core.validate_input(_room()) == []


def test_validate_zero_size():
    """면적 0 은 오류 메시지를 돌려준다."""
    assert "면적은 5㎡ 이상 100㎡ 이하로 입력해 주세요" in core.validate_input(_room(size_m2=0))


def test_validate_zero_rent():
    """월세 0 은 오류 메시지를 돌려준다."""
    assert "월세는 1만원 이상 300만원 이하로 입력해 주세요" in core.validate_input(_room(monthly_rent=0))
