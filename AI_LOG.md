# AI 활용 기록 (AI_LOG.md) — 커밋할 때마다 채운다

| # | 시각 | 목적 (US-ID) | 프롬프트 요약 | 검증 · 수정 | 채택 |
|---|------|--------------|---------------|-------------|------|
| 1 | 10/23 13:40 | US-0 뼈대 | **서버 밖 AI**(claude.ai 웹 Claude Code 세션)에 과제 양식(docx)·교수 예시 3개를 주고 주제 제안과 프로젝트 뼈대 요청 → 주제·CLAUDE.md·SPEC.md·data/rooms.csv(가상)·빈 화면 생성 | (직접 확인 후 적기: 예) 서버에서 CLAUDE.md·SPEC.md를 직접 읽음, streamlit run app.py 로 홈 확인) | 채택 |
| 2 | | US-1 | | | |
| 3 | 10/23 05:47 | US-2 매물 입력 화면 | SPEC US-2대로 pages/1_매물입력.py 요청(지역·방 형태 선택지는 데이터에서, 검증은 core.validate_input, 통과 시 session_state["room"] 저장, 이 파일만 수정) | 문법 검사 통과, pytest 9 passed, git status로 이 파일만 바뀐 것 확인. (직접 확인 후 적기: streamlit run app.py 로 기본값 저장 / 면적 0·월세 0 경고 확인 결과) | (확인 후 적기) |
| 4 | 10/23 05:37 | US-3 계산 로직 | SPEC 계산 규칙대로 core.py 함수 4개와 테스트(기대값 5개, 예외 2개) 요청 | pytest 9 passed, git status로 두 파일(core.py, test_core.py)만 바뀐 것 확인, 기본 시나리오 47.5/38.5/+23.4%/비쌈 직접 대조 | 채택 |
| 5 | | US-4 | | | |

- "거부한 제안"과 "AI가 틀린 사례"가 있어야 검증했다는 증거가 된다 (루브릭 15점). → 제출 양식 2-4, 3-3에 그대로 옮긴다.
- SPEC.md의 "검증용 기대값" 표와 다르게 나오면 그게 바로 "AI가 틀린 사례"다. 무엇이 달랐고 어떻게 고쳤는지 적는다.
- 대화 이력(`claude -c`)은 로그아웃 후 사라질 수 있다 — 기록은 이 파일에.
- #1 은 서버 Claude Code 로그(`log/claude`)에 없으므로 제출 양식 **3-2 "Claude Code 밖에서 쓴 AI"** 칸에도 적는다. #2부터는 학교 서버 Claude Code.
