# 1주차 회고

## 1. 이번 주에 만든 것

- ex1_file_organizer.py: 폴더 바로 아래 파일들을 확장자별 하위 폴더(images/docs/videos/etc)로 옮기는 스크립트. 중복 파일은 건너뛰고 하위 폴더는 건드리지 않는다.
- ex2_quotes_crawler.py: quotes.toscrape.com 10페이지를 순회해 명언 100건(본문·저자·태그)을 CSV로 저장하고, 저자별 TOP 5를 집계하는 크롤러.

## 2. 내 말로 설명하기 (각 2~3문장)

### continue 와 return 의 차이
continue는 조건에 안 맞는 항목을 건너뛰고 for문의 다음 항목으로 넘어간다. for문 자체는 계속 돈다.
return은 for문이 아니라 함수 전체를 끝내고 값을 돌려준다. 그 뒤 줄은 실행되지 않는다.

### requests.get 에 timeout 을 왜 붙이나
상대 서버가 응답을 안 줄 때 무한정 기다리지 않게 끊는 보험이다.
안 붙이면 프로세스가 영원히 멈춰 있어서 실패했다는 사실조차 모른다.

### raise_for_status 가 없으면 무슨 일이 생기나
에러가 안 난다. 404 페이지도 HTML이라 그대로 파싱되고, div.quote가 0개라 "0건 수집"으로 조용히 정상 종료된다.
그래서 위험하다. 새벽에 크론이 돌면 아침에 CSV는 비어 있는데 로그에 실패 흔적이 없어서, 사이트가 죽은 건지 코드가 틀린 건지 알 수 없다. raise_for_status는 그 자리에서 크게 터뜨려서 실패를 바로 알게 한다.

### select 와 select_one 의 차이
select는 조건에 맞는 것 전부를 리스트로, select_one은 그중 첫 번째([0]) 하나만 객체로 돌려준다.
리스트에는 .get_text()를 바로 못 붙이니, 하나만 필요하면 select_one을 쓴다.

### [식 for x in 리스트] 를 for문으로 풀면
result = []
for x in [1,2,3]:
    result.append(x * 2)


### "li.next > a" 에서 > 의 뜻
부모 바로 아래 

## 3. 막혔던 곳과 어떻게 풀었나
- fetch_page 확인 명령을 돌렸는데 NotImplementedError가 남.
  에러 마지막 줄의 `line 31, raise NotImplementedError`를 보고 함수를 아직 안 채운 걸 확인.
  3줄 채우고 재실행해서 10이 찍히는 걸로 해결.
  배운 것: 에러는 마지막 줄부터 읽고, 파일명:줄번호로 위치를 찾는다.
- ",".join([...]) 줄이 안 읽혔음.
  안쪽부터 실행되는 순서가 헷갈렸고, REPL에서 select → 컴프리헨션 → join을 한 단계씩 쳐 보며 풀었다.
  배운 것: 겹친 한 줄은 안쪽부터 쪼개서 본다.

## 4. 실무 습관 체크 (README "몸에 붙여야 할 습관")

- [x] requests.get 에 timeout 항상 지정 (fetch_page에 timeout=10)
- [x] 페이지 사이 sleep 으로 서버 배려 (crawl_all에 time.sleep(0.5))
- [x] 파싱(parse_quotes)과 저장(save_csv) 함수 분리 (저장 방식이 바뀌어도 파싱은 안 건드린다)
- [x] 과제마다 커밋 (ex1 1개, ex2 4개, 연습 2개)

## 5. 다음 주(Playwright)에 가져갈 것

- CSS 셀렉터(div.quote, li.next > a)는 Playwright의 page.locator()에 그대로 쓴다. 이번 주 배운 select/select_one 감각이 곧 locator 감각이다.
- "받아오기(fetch) → 뽑기(parse) → 저장(save)" 세 함수 분리 구조는 브라우저 자동화에서도 같다. fetch 자리만 requests에서 Playwright로 바뀐다.
- 막히면 REPL에서 한 단계씩 값을 찍어 본다. Playwright는 headed 모드로 눈으로 보는 게 그 역할.
