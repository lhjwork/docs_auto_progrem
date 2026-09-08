"""리스트 컴프리헨션 연습 (Day 4 보충)

[식 for 변수 in 리스트]  ==  for문으로 리스트 만들기를 한 줄로 압축한 것.

    result = []
    for x in 리스트:
        result.append(식)

이 3줄이 [식 for x in 리스트] 한 줄과 완전히 같다.
읽는 순서: 오른쪽 for부터. "리스트의 각 원소를 x라 하고, 각 x에 대해 식을 모아라"

아래 TODO를 for문 버전과 컴프리헨션 버전 둘 다 채우고 `python practice_listcomp.py` → PASS.
"""

# ---------- 예제 (읽기만) ----------
nums = [1, 2, 3]

# for문 버전
doubled_for = []
for n in nums:              # 1번째: n=1 → append(2) / 2번째: n=2 → append(4) / 3번째: n=3 → append(6)
    doubled_for.append(n * 2)

# 컴프리헨션 버전 (같은 결과)
doubled = [n * 2 for n in nums]   # → [2, 4, 6]

assert doubled_for == doubled == [2, 4, 6]


# ---------- 연습 1: 각 단어의 길이 ----------
words = ["change", "deep-thoughts", "thinking", "world"]

# TODO: for문으로 lengths_for 만들기 (힌트: len(w))
lengths_for = []
for w in words:
    lengths_for.append(len(w))
# 여기에 for문 작성

# TODO: 컴프리헨션 한 줄로 lengths 만들기

lengths = [len(w) for w in words]

assert lengths_for == [6, 13, 8, 5], f"for문 버전: {lengths_for}"
assert lengths == [6, 13, 8, 5], f"컴프리헨션 버전: {lengths}"


# ---------- 연습 2: 대문자로 ----------
# TODO: 컴프리헨션으로 ["CHANGE", "DEEP-THOUGHTS", ...] 만들기 (힌트: w.upper())
upper = [w.upper() for w in words]

assert upper == ["CHANGE", "DEEP-THOUGHTS", "THINKING", "WORLD"], f"실제: {upper}"


# ---------- 연습 3: 딕셔너리 리스트에서 값 꺼내기 (과제와 같은 모양) ----------
# q.select("a.tag") 가 돌려주는 것도 "객체들의 리스트"고, t.get_text() 로 안의 값을 꺼낸다.
# 여기선 딕셔너리로 흉내낸다. t.get_text() 대신 t["name"] 이라고 생각하면 됨.
tags = [{"name": "change"}, {"name": "deep-thoughts"}, {"name": "thinking"}]

# TODO: 컴프리헨션으로 ["change", "deep-thoughts", "thinking"] 만들기
names = [t["name"] for t in tags]

assert names == ["change", "deep-thoughts", "thinking"], f"실제: {names}"

# TODO: 위 names 를 쉼표로 합쳐 문자열 하나로 (힌트: ",".join(...))
joined = ",".join(names)

assert joined == "change,deep-thoughts,thinking", f"실제: {joined}"


# ---------- 연습 4 (도전): 조건 붙이기 ----------
# [식 for x in 리스트 if 조건]  → 조건이 참인 것만 모은다
# TODO: words 중 길이가 6 이상인 것만 모으기
long_words = [w for w in words if len(w) >= 6]

assert long_words == ["change", "deep-thoughts", "thinking"], f"실제: {long_words}"

print("PASS ✅ 리스트 컴프리헨션 연습 완료")
