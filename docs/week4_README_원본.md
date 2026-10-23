# 4주차 실습 파일 — 개인 프로젝트 개발 워크숍 (내 프로젝트 폴더에 넣을 것)

```bash
cd ~/work/<내 프로젝트>                       # 3주차 churn_check 복사본 또는 새 폴더 (~/work 안)
cp ~/work/shared/week4/CLAUDE.md .            # AI 규칙 파일 → 내 주제로 수정 (체크포인트 1 직후, 가장 먼저)
cp ~/work/shared/week4/.gitignore .
cp ~/work/shared/week4/AI_LOG.md .            # AI 활용 기록 (커밋마다 채운다)
cp ~/work/shared/templates/02_기능_명세서_템플릿.md SPEC.md   # 0:40 제출
mkdir -p .streamlit && cp ~/work/shared/week4/secrets.toml.example .streamlit/secrets.toml   # 비밀값이 있을 때만
git add . && git commit -m "US-0: 규칙 파일·명세·기록 뼈대"
```

| 파일 | 쓰임 (슬라이드) |
|---|---|
| `CLAUDE.md` | Claude Code가 매 요청마다 읽는 프로젝트 규칙 — 구조·규칙·하지 말 것·검증 한 화면 (PART 3) |
| `.gitignore` | 이력에 넣지 않을 것: `__pycache__/` · `.streamlit/secrets.toml` · `app.log` (PART 2) |
| `secrets.toml.example` | `.streamlit/secrets.toml`의 본보기 — 수업용 키만 (PART 2 규칙 5) |
| `AI_LOG.md` | AI 활용 기록 — 5주차 Q&A에서 교수가 연다 (PART 3) |
| `SPEC.md` ← templates/02 | 사용자 스토리·MoSCoW·완료 조건·진행표 (PART 1, 0:40 제출) |

워크숍 리듬: 작업 하나 → 실행 확인 → `git commit -m "US-N: …"` → 다음. 앱 재시작은 앱 터미널 `Ctrl+C` → `streamlit run app.py`. 시연 24시간 전 `git tag stage1-final`.
