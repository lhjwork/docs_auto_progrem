"""다리 Day C: 에러 메시지만 보고 혼자 고치기

이 파일에는 일부러 넣은 버그가 6개 있다. 실행하면 첫 번째 버그에서 죽는다.
고치면 다음 버그에서 죽는다. 6개 다 고치면 PASS.

읽는 법 (매번 이 순서):
  1. 터미널 출력 맨 마지막 줄 → 에러 종류와 메시지
  2. 그 바로 위 → File "...day_c_errors.py", line N  ← 줄 번호
  3. 그 줄만 본다. 다른 데 보지 않는다.
  4. 에러 종류별 뜻:
     NameError      : 그 이름의 변수/함수가 없다 (오타 확률 90%)
     TypeError      : 타입이 안 맞는다 (문자열 + 숫자, 리스트에 .get_text() 등)
     KeyError       : 딕셔너리에 그 키가 없다
     IndexError     : 리스트에 그 번호 칸이 없다
     AttributeError : 그 객체엔 그런 메서드/속성이 없다

규칙: Claude 에게 묻지 않는다. 30분 이상 막힌 것만 묻되, 그때도 "에러 마지막 줄"을 같이 붙인다.
"""
from collections import Counter

quotes = [
    {"text": "The world as we have created it", "author": "Albert Einstein", "tags": "change,thinking"},
    {"text": "It is our choices", "author": "J.K. Rowling", "tags": "abilities,choices"},
    {"text": "Imperfection is beauty", "author": "Marilyn Monroe", "tags": "be-yourself"},
]

# ---- 버그 1 ----
total = len(qoutes)
assert total == 3

# ---- 버그 2 ----
message = "수집 건수: " + total
assert message == "수집 건수: 3"

# ---- 버그 3 ----
first_author = quotes[0]["Author"]
assert first_author == "Albert Einstein"

# ---- 버그 4 ----
last = quotes[3]
assert last["author"] == "Marilyn Monroe"

# ---- 버그 5 ----
tags = quotes[1]["tags"].split(",")
first_tag = tags.upper()
assert first_tag == "ABILITIES"

# ---- 버그 6 ----
counts = Counter([q["author"] for q in quotes])
top = counts.most_common(1)
assert top == ("Albert Einstein", 1), f"실제: {top}"   # 힌트: most_common 은 리스트를 돌려준다. [0] 이 빠졌나?

print("PASS ✅ Day C 완료 — 6개 버그를 혼자 고쳤다. 커밋하세요")
