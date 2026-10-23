# AI 활용 기록 (AI_LOG.md) — 커밋할 때마다 채운다

| # | 시각 | 목적 (US-ID) | 프롬프트 요약 | 검증 · 수정 | 채택 |
|---|------|--------------|---------------|-------------|------|
| 1 | 10/23 13:40 | US-0 뼈대 | **서버 밖 AI**(claude.ai 웹 Claude Code 세션)에 과제 양식(docx)·교수 예시 3개를 주고 주제 제안과 프로젝트 뼈대 요청 → 주제·CLAUDE.md·SPEC.md·data/rooms.csv(가상)·빈 화면 생성 | (직접 확인 후 적기: 예) 서버에서 CLAUDE.md·SPEC.md를 직접 읽음, streamlit run app.py 로 홈 확인) | 채택 |
| 2 | | US-1 | | | |
| 3 | 10/23 05:47 | US-2 매물 입력 화면 | SPEC US-2대로 pages/1_매물입력.py 요청(지역·방 형태 선택지는 데이터에서, 검증은 core.validate_input, 통과 시 session_state["room"] 저장, 이 파일만 수정) | 문법 검사 통과, pytest 9 passed, git status로 이 파일만 바뀐 것 확인. Streamlit AppTest(브라우저 없이 화면 실행)로 확인: 선택지가 데이터에서 읽힘(지역 4·방 형태 3), 기본값 제출 시 session_state["room"] 저장, 면적 0·월세 0은 SPEC 문구 경고 후 저장 안 됨. (직접 확인 후 적기: streamlit run app.py 브라우저 화면) | 채택 |
| 4 | 10/23 05:37 | US-3 계산 로직 | SPEC 계산 규칙대로 core.py 함수 4개와 테스트(기대값 5개, 예외 2개) 요청 | pytest 9 passed, git status로 두 파일(core.py, test_core.py)만 바뀐 것 확인, 기본 시나리오 47.5/38.5/+23.4%/비쌈 직접 대조 | 채택 |
| 5 | 10/23 05:55 | US-4 진단 결과 화면 | SPEC US-4대로 pages/2_진단결과.py 요청(session_state["room"]을 읽어 find_similar·judge로 계산, metric 2개·판정 문구·근거 3줄·비교 매물 표, 입력 없으면 st.warning, 이 파일만 수정) | pytest 9 passed, git status로 이 파일만 바뀐 것 확인, AppTest로 기대값 1번(47.5/38.5/+23.4%/비쌈)·5번(37.5/33.75/+11.1%/비쌈, 10건) 대조, 입력 없음 경고 문구 확인. 설치된 Streamlit이 use_container_width 폐지 경고를 내서 width="stretch"로 바꿈. 입력 화면 기본값 제출 후 결과 화면까지 이어서 확인: metric 47.5만원(+23.4%)/38.5만원, 비쌈 판정, 근거 3줄, 비교 매물 10행, 입력 없이 열면 경고. (직접 확인 후 적기: streamlit run app.py 브라우저 화면) | 채택 |
| 6 | 10/23 06:06 | US-5 막대 차트 | SPEC US-5대로 결과 화면에 비교 매물 환산 월 비용 막대 차트를 st.bar_chart 로 추가 요청(새 패키지 금지) | pytest 9 passed, git status로 pages/2_진단결과.py 하나만 바뀐 것 확인, AppTest로 기대값 1번·5번 입력에서 예외 없이 막대 차트 생성(x=room_id, y=monthly_cost, 내 매물 색 구분, 비용 오름차순 정렬) 확인. (직접 확인 후 적기: streamlit run app.py 브라우저에서 막대 11개·내 매물 색 구분·x축 글자 겹침 여부) | (확인 후 적기) |

- "거부한 제안"과 "AI가 틀린 사례"가 있어야 검증했다는 증거가 된다 (루브릭 15점). → 제출 양식 2-4, 3-3에 그대로 옮긴다.
- SPEC.md의 "검증용 기대값" 표와 다르게 나오면 그게 바로 "AI가 틀린 사례"다. 무엇이 달랐고 어떻게 고쳤는지 적는다.
- 대화 이력(`claude -c`)은 로그아웃 후 사라질 수 있다 — 기록은 이 파일에.
- #1 은 서버 Claude Code 로그(`log/claude`)에 없으므로 제출 양식 **3-2 "Claude Code 밖에서 쓴 AI"** 칸에도 적는다. #2부터는 학교 서버 Claude Code.
