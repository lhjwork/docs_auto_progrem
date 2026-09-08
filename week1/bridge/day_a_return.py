"""다리 Day A: 함수와 반환값

1주차에서 "return 줄이 왜 10을 내나"가 헷갈렸다. 핵심은 하나다:

    함수 호출 f(x) 는 실행이 끝나면 그 자리가 return 값으로 바뀐다.

    print(len(fetch_page(url).select("div.quote")))
    → fetch_page(url) 자리가 soup 로 바뀜
    → soup.select(...) 자리가 리스트로 바뀜
    → len(리스트) 자리가 10 으로 바뀜
    → print(10)

아래 TODO 를 채우고 `python bridge/day_a_return.py` → PASS.
파트 1은 "값 예측", 파트 2는 "함수 작성". 예측은 실행 전에 종이에 먼저 쓰고 맞춰 볼 것.
"""

# ==================== 파트 1: 값 예측 ====================
# 각 함수를 읽고, 호출 결과가 뭔지 expected 에 적는다. 실행해 보기 전에 먼저 적을 것.

def double(n):
    return n * 2

expected_1 = None            # TODO: double(4) 의 값
assert expected_1 == double(4), "예측이 틀렸다. 종이에 다시 따라가 볼 것"


def double_twice(n):
    return double(double(n))  # 안쪽 double 이 먼저 → 그 결과가 바깥 double 로

expected_2 = None            # TODO: double_twice(3) 의 값
assert expected_2 == double_twice(3), "예측이 틀렸다. 종이에 다시 따라가 볼 것"


def first_word(text):
    words = text.split()      # "hello big world" → ["hello", "big", "world"]
    return words[0]

expected_3 = None            # TODO: first_word("hello big world") 의 값 (문자열)
assert expected_3 == first_word("hello big world")


def count_words(text):
    return len(text.split())

expected_4 = None            # TODO: count_words("a b c d") 의 값
assert expected_4 == count_words("a b c d")


def no_return(n):
    n * 2                     # return 이 없다!

expected_5 = "???"           # TODO: no_return(4) 의 값. 힌트: return 없는 함수는 None 을 돌려준다
assert expected_5 == no_return(4), "예측이 틀렸다. 종이에 다시 따라가 볼 것"


def early_return(items):
    for x in items:
        if x > 10:
            return x          # 여기서 함수 전체가 끝남. for 도 끝
    return None               # for 가 다 돌았는데 못 찾으면

expected_6 = None            # TODO: early_return([3, 15, 20]) 의 값. 15? 20? 리스트?
assert expected_6 == early_return([3, 15, 20]), "예측이 틀렸다. 종이에 다시 따라가 볼 것"

expected_7 = "???"           # TODO: early_return([1, 2, 3]) 의 값
assert expected_7 == early_return([1, 2, 3]), "예측이 틀렸다. 종이에 다시 따라가 볼 것"


# ==================== 파트 2: 함수 작성 ====================

def add(a, b):
    """두 수의 합을 반환"""
    # TODO
    raise NotImplementedError

assert add(2, 3) == 5


def longest(words):
    """단어 리스트에서 가장 긴 단어를 반환. 힌트: max(words, key=len)"""
    # TODO
    raise NotImplementedError

assert longest(["a", "abc", "ab"]) == "abc"


def find_author(quotes, text_part):
    """quotes(딕셔너리 리스트)에서 text 에 text_part 가 들어 있는 첫 항목의 author 를 반환.
    못 찾으면 None.
    힌트: early_return 과 같은 모양. for → if text_part in q["text"] → return q["author"]
    """
    # TODO
    raise NotImplementedError

sample = [
    {"text": "The world as we have created it", "author": "Albert Einstein"},
    {"text": "It is our choices", "author": "J.K. Rowling"},
]
assert find_author(sample, "choices") == "J.K. Rowling"
assert find_author(sample, "world") == "Albert Einstein"
assert find_author(sample, "없는말") is None


def summarize(quotes):
    """quotes 의 건수와 첫 저자를 튜플로 반환: (건수, 첫 저자)
    힌트: return len(quotes), quotes[0]["author"]   ← 콤마로 두 값을 한 번에 반환
    """
    # TODO
    raise NotImplementedError

count, first = summarize(sample)   # 튜플을 두 변수로 풀어 받기
assert count == 2 and first == "Albert Einstein"

print("PASS ✅ Day A 완료 — 커밋하세요")
