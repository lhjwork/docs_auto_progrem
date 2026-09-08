"""1주차 과제 2: 정적 페이지 크롤러 (Day 3~5)

목표: https://quotes.toscrape.com (크롤링 연습용 공개 사이트)에서
명언 목록을 수집해 CSV로 저장.

배우는 것: requests, BeautifulSoup, CSS selector, 페이지네이션, CSV 저장.
이게 3주차 Playwright 프로젝트의 기초 체력이 된다.

TODO를 채우고 `python ex2_quotes_crawler.py` 실행 → "PASS" 뜨면 완료.
결과물: quotes.csv (100건)
"""

import csv
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


def fetch_page(url: str) -> BeautifulSoup:
    """URL을 가져와 BeautifulSoup 객체로 반환.

    요구사항:
    1. timeout=10 지정 (실무 습관: timeout 없는 requests는 금지)
    2. resp.raise_for_status() 로 HTTP 에러 시 예외 발생
    """
    # TODO: 구현하세요. 힌트: requests.get(...), BeautifulSoup(resp.text, "html.parser")

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def parse_quotes(soup: BeautifulSoup) -> list[dict]:
    """페이지 하나에서 명언 목록 추출.

    반환 형식: [{"text": ..., "author": ..., "tags": "tag1,tag2"}, ...]

    힌트: 브라우저 개발자도구로 구조를 먼저 봐라 (이게 크롤링의 8할).
    - 명언 블록: div.quote
    - 본문: span.text / 저자: small.author / 태그: a.tag (여러 개)
    - soup.select("div.quote"), q.select_one("span.text").get_text()
    """
    results = []
    for q in soup.select("div.quote"):
        text = q.select_one("span.text").get_text()
        author = q.select_one("small.author").get_text()
        tags = ",".join([t.get_text() for t in q.select("a.tag")])
        results.append({"text": text, "author": author, "tags": tags})
    return results


def next_page_url(soup: BeautifulSoup) -> str | None:
    """다음 페이지가 있으면 절대 URL, 없으면 None.

    힌트: li.next > a 의 href 속성. BASE_URL + href
    """
    # TODO: 구현하세요.
    next_page = soup.select_one("li.next > a")
    if next_page:
        return BASE_URL + next_page["href"]
    return None

def crawl_all() -> list[dict]:
    """전체 페이지 순회. 페이지 사이 time.sleep(0.5) — 상대 서버 배려는 기본기."""
    quotes = []
    url = BASE_URL
    while url:
        soup = fetch_page(url)
        quotes.extend(parse_quotes(soup))
        url = next_page_url(soup)
        if url:
            time.sleep(0.5)
        print(f"수집 {len(quotes)}건...")
    return quotes


def save_csv(quotes: list[dict], path: Path):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes)


def _self_check():
    quotes = crawl_all()
    assert len(quotes) == 100, f"전체 100건이어야 함, 실제: {len(quotes)}"
    first = quotes[0]
    assert "Einstein" in first["author"], f"1번 저자는 Einstein, 실제: {first['author']}"
    assert first["text"].strip(), "text가 비어있음"
    assert "," in quotes[0]["tags"] or quotes[0]["tags"], "tags는 쉼표로 합친 문자열"
    out = Path(__file__).parent / "quotes.csv"
    save_csv(quotes, out)
    print(f"PASS ✅ ex2 완료 — {out} 저장됨. 커밋하세요")


if __name__ == "__main__":
    _self_check()
