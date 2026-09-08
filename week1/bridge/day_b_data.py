"""다리 Day B: 리스트·딕셔너리 넣고 꺼내고 세기

크롤러가 다루는 데이터는 결국 "딕셔너리의 리스트"다:
    [{"text": ..., "author": ..., "tags": ...}, {...}, ...]
이걸 자유롭게 넣고 꺼내고 세는 게 오늘 목표.

TODO 채우고 `python bridge/day_b_data.py` → PASS.
끝나면 `python practice_unpack.py` 도 PASS 시킬 것 (Day B 두 번째 파일).
"""
from collections import Counter

quotes = [
    {"author": "Albert Einstein", "tags": "change,thinking"},
    {"author": "J.K. Rowling",    "tags": "abilities,choices"},
    {"author": "Albert Einstein", "tags": "inspirational,life"},
    {"author": "Jane Austen",     "tags": "love"},
    {"author": "Albert Einstein", "tags": "life,simile"},
]

# ---------- 1. 리스트 기본 ----------
n = None                     # TODO: quotes 의 건수
first = None                 # TODO: 첫 번째 항목 (딕셔너리)
last = None                  # TODO: 마지막 항목. 힌트: 인덱스 -1

assert n == 5
assert first["author"] == "Albert Einstein"
assert last["author"] == "Albert Einstein" and last["tags"] == "life,simile"


# ---------- 2. 딕셔너리 꺼내기 ----------
second_author = None         # TODO: 두 번째 항목의 author
second_tags = None           # TODO: 두 번째 항목의 tags 를 쉼표로 쪼갠 리스트. 힌트: .split(",")

assert second_author == "J.K. Rowling"
assert second_tags == ["abilities", "choices"]


# ---------- 3. 컴프리헨션으로 한 열만 뽑기 ----------
authors = None               # TODO: author 만 모은 리스트 (길이 5)

assert authors == ["Albert Einstein", "J.K. Rowling", "Albert Einstein", "Jane Austen", "Albert Einstein"]


# ---------- 4. 조건으로 거르기 ----------
einstein_only = None         # TODO: author 가 "Albert Einstein" 인 항목만 (딕셔너리 리스트, 길이 3)

assert len(einstein_only) == 3
assert all(q["author"] == "Albert Einstein" for q in einstein_only)


# ---------- 5. 세기 ----------
counts = None                # TODO: Counter 로 저자별 건수
top1 = None                  # TODO: counts.most_common(1)[0]  → ("Albert Einstein", 3)

assert counts["Albert Einstein"] == 3 and counts["Jane Austen"] == 1
assert top1 == ("Albert Einstein", 3)


# ---------- 6. 새 항목 추가 ----------
# TODO: quotes 에 {"author": "Mark Twain", "tags": "humor"} 를 append
assert len(quotes) == 6 and quotes[-1]["author"] == "Mark Twain"


# ---------- 7. 딕셔너리 새로 만들기 ----------
# author → 그 저자의 첫 tags 문자열. 예: {"Albert Einstein": "change,thinking", ...}
# 힌트: 빈 dict 만들고 for 돌며 `if q["author"] not in d: d[q["author"]] = q["tags"]`
first_tags_by_author = None  # TODO

assert first_tags_by_author["Albert Einstein"] == "change,thinking"
assert first_tags_by_author["Mark Twain"] == "humor"
assert len(first_tags_by_author) == 4


# ---------- 8. 모든 태그 펼쳐서 세기 (도전) ----------
# 각 항목의 tags 를 split 해서 전부 한 리스트에 모은 뒤 Counter.
# 힌트: 이중 for 또는 [t for q in quotes for t in q["tags"].split(",")]
tag_counts = None            # TODO

assert tag_counts["life"] == 2, f"life 는 2번: {tag_counts}"
assert tag_counts["humor"] == 1

print("PASS ✅ Day B 완료 — practice_unpack.py 도 PASS 시킨 뒤 커밋하세요")
