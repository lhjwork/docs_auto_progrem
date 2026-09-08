"""겹친 한 줄 쪼개기 연습 (Day 7 보충)

규칙: 한 줄에 여러 호출이 겹쳐 있으면 안쪽부터 한 단계씩 변수에 담아 푼다.
푼 결과가 원래 한 줄과 같으면 assert 가 통과한다.

예제 (읽기만):
    원본: total = len(",".join(["a", "b"]))
    쪼갠 것:
        step1 = ",".join(["a", "b"])   # → "a,b"
        step2 = len(step1)             # → 3
    assert step2 == total
"""

# ---------- 연습 1 ----------
words = ["change", "deep-thoughts", "thinking"]
original = ",".join([w.upper() for w in words])

# TODO: 두 단계로 쪼개기
step1 = None   # 컴프리헨션 결과 (리스트)
step2 = None   # join 결과 (문자열)

assert step1 == ["CHANGE", "DEEP-THOUGHTS", "THINKING"], f"step1: {step1}"
assert step2 == original, f"step2: {step2}"


# ---------- 연습 2 ----------
quotes = [{"author": "Einstein"}, {"author": "Rowling"}, {"author": "Einstein"}]
original = len([q["author"] for q in quotes if q["author"] == "Einstein"])

# TODO: 두 단계로 쪼개기
step1 = None   # 조건 붙은 컴프리헨션 결과 (리스트)
step2 = None   # len 결과 (숫자)

assert step1 == ["Einstein", "Einstein"], f"step1: {step1}"
assert step2 == original == 2, f"step2: {step2}"


# ---------- 연습 3 (과제 코드 그대로) ----------
from bs4 import BeautifulSoup
html = '<div class="quote"><a class="tag">love</a><a class="tag">life</a></div>'
q = BeautifulSoup(html, "html.parser")
original = ",".join([t.get_text() for t in q.select("a.tag")])

# TODO: 세 단계로 쪼개기
step1 = None   # select 결과 (a 태그 리스트)
step2 = None   # get_text 뽑은 결과 (문자열 리스트)
step3 = None   # join 결과

assert len(step1) == 2, f"step1: {step1}"
assert step2 == ["love", "life"], f"step2: {step2}"
assert step3 == original == "love,life", f"step3: {step3}"

print("PASS ✅ 쪼개기 연습 완료")
