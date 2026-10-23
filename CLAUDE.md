# 프로젝트: 방값체크 — 수원대 주변 자취방 월세 적정가 진단 (Streamlit)
자취방을 구하는 대학생을 위해, 매물 조건을 넣으면 비슷한 매물 시세와 비교해 적정 월세와 판정 근거를 알려 주는 서비스.
명세는 SPEC.md, 데이터 열 목록은 data/README.md 를 따른다.

## 구조
- app.py 홈, pages/1_매물입력.py 입력, pages/2_진단결과.py 결과, core.py 로직(streamlit import 금지), data/rooms.csv
- 데이터 로드는 화면 쪽에서 @st.cache_data 로 감싸서 core.load_data() 호출, 경로는 app.py 기준 상대 경로
- 입력값은 st.session_state["room"] 에 dict 로 저장하고 결과 화면에서 읽는다
- 테스트는 test_core.py (core.py 함수만 테스트)

## 코딩 규칙
- Python 3, streamlit, pandas. 새 패키지는 설치하기 전에 먼저 물어볼 것 (설치하면 requirements.txt에도 추가)
- 함수에는 한글 docstring, 화면 문구는 한국어 존댓말
- 빈 결과·잘못된 입력에서 오류 대신 st.warning
- 열 이름은 data/README.md의 목록만 사용 (지어내지 말 것)
- 금액 단위는 모두 "만원", 환산 월 비용 = 월세 + 관리비 + 보증금 × 0.06 / 12 (전환율 상수 RATE = 0.06 은 core.py 맨 위에)
- 한 번에 US 하나만 작업하고, 끝나면 무엇을 바꿨는지 파일별로 요약할 것

## 하지 말 것
- 요청한 파일 외 수정, 전체 재작성, 비밀값 하드코딩
- data/rooms.csv 내용 수정 (읽기만)
- 이 프로젝트 폴더(rent_check) 밖의 파일 접근, rm -rf / sudo 실행 (예외: 제출 직전 내가 요청하면 ~/.claude/projects 를 log/claude 로 복사만 한다)
- git commit / push 는 내가 확인하고 "커밋해 줘"라고 할 때만 한다 (메시지는 "US-N: …" 형식)

## 검증
- core.py 수정 시 python -m pytest -q 를 실행해 결과를 알려 줄 것
- 화면 파일 수정 후에는 streamlit AppTest 로 오류 없이 열리는지만 확인하고, "push 후 공개 주소에서 직접 확인하라"고 알려 줄 것 (화면 확인은 내가 한다)
- SPEC.md의 "검증용 기대값" 표와 계산 결과가 다르면 고치기 전에 먼저 알려 줄 것
