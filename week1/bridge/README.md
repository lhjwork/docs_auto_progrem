# 다리 3일: 2주차 전에 잡을 세 가지

1주차에서 흔들린 딱 세 곳만 잡는다. 하루 1시간이면 된다.

| Day | 파일 | 잡는 것 | 완료 기준 |
|---|---|---|---|
| A | `day_a_return.py` | 함수 반환값이 호출자에게 흘러가는 그림 | PASS |
| B | `day_b_data.py` + `../practice_unpack.py` | 리스트·딕셔너리 넣고 꺼내고 세기 | 둘 다 PASS |
| C | `day_c_errors.py` | 에러 메시지만 보고 혼자 고치기 | PASS, **Claude에게 안 묻고** |

## 규칙

- Day A, B는 막히면 Claude에게 물어도 된다. 단 "답 말고 힌트".
- Day C는 다르다. 에러 마지막 줄 → 파일명:줄번호 → 그 줄만 본다. 30분 넘게 막힌 것만 묻는다.
- 매일 끝나면 커밋. 메시지 예: `다리 A: 반환값 연습 통과`

## 세팅

```bash
cd ~/Desktop/projects/ajung/week1 && source .venv/bin/activate
python bridge/day_a_return.py
```
