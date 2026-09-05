# 1주차: Python 자동화 기본기

## 세팅 (완료됨)

```bash
cd week1
source .venv/bin/activate   # 매 세션 시작 시
```

## 일정 (하루 ~2시간)

| Day | 할 일 | 완료 기준 |
|---|---|---|
| 1~2 | `ex1_file_organizer.py` TODO 구현 | `python ex1_file_organizer.py` → PASS |
| 3 | quotes.toscrape.com 을 브라우저 개발자도구(F12)로 뜯어보기 + `fetch_page` 구현 | HTML 구조를 말로 설명할 수 있음 |
| 4 | `parse_quotes`, `next_page_url` 구현 | 1페이지 10건 파싱 성공 |
| 5 | 전체 크롤링 완주 | `python ex2_quotes_crawler.py` → PASS, quotes.csv 100건 |
| 6 | 도전 과제 (아래) | 선택 |
| 7 | 배운 것 정리 + git 커밋 정리 | CURRICULUM.md 1주차 체크 |

## 규칙

- 막히면 30분은 스스로 부딪히고, 그다음 Claude에게 "답 말고 힌트"를 요청할 것.
  답을 받아 적으면 3주차 Playwright에서 무너진다.
- 과제 하나 끝날 때마다 커밋. 커밋 메시지는 "뭘 왜 했는지" 한 줄.

## 도전 과제 (Day 6, 선택)

ex2를 확장: 저자별 명언 수를 집계해서 상위 5명을 출력하는 `top_authors()` 추가.
힌트: `collections.Counter` — 직접 dict로 세지 말 것 (stdlib 먼저).

## 이번 주에 몸에 붙여야 할 실무 습관

1. `requests.get`에 timeout 항상 지정
2. 크롤링 대상 서버 배려 (sleep, 과도한 요청 금지)
3. 파싱 로직과 저장 로직 분리 (함수 단위)
4. 매일 커밋
