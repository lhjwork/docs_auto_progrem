"""1주차 과제 1: 파일 자동 정리 스크립트 (Day 1~2)

목표: 폴더 안의 파일들을 확장자별 하위 폴더로 옮기는 스크립트.
자동화의 가장 기본 형태 — "반복되는 손작업을 코드로".

배우는 것: pathlib, shutil, 예외처리 습관.

TODO를 채우고 `python ex1_file_organizer.py` 로 실행하면
스스로 테스트 폴더를 만들어 검증해준다. "PASS"가 뜨면 완료.
"""

import shutil
import tempfile
from pathlib import Path

# 확장자 → 폴더 이름 매핑. 여기 없는 확장자는 "etc"로.
CATEGORIES = {
    ".jpg": "images", ".png": "images", ".gif": "images",
    ".pdf": "docs", ".docx": "docs", ".xlsx": "docs",
    ".mp4": "videos", ".mov": "videos",
    ".zip": "archives",
}


def organize(folder: Path) -> int:
    """folder 바로 아래의 파일들을 카테고리 폴더로 이동. 옮긴 파일 수를 반환.

    요구사항:
    1. folder 바로 아래의 '파일'만 대상 (하위 폴더는 건드리지 않음)
    2. 확장자(소문자 기준)로 CATEGORIES에서 폴더명을 찾고, 없으면 "etc"
    3. 대상 폴더가 없으면 만들 것 (mkdir(exist_ok=True))
    4. 같은 이름 파일이 이미 있으면 덮어쓰지 말고 건너뛸 것 (옮긴 수에 미포함)
    """
    moved = 0
    # TODO: 여기를 구현하세요.
    # 힌트: folder.iterdir(), p.is_file(), p.suffix.lower(),
    #       shutil.move(str(src), str(dst))
    return moved


def _self_check():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ["a.jpg", "b.PDF", "c.mp4", "d.xyz", "e.zip"]:
            (root / name).write_text("x")
        (root / "subdir").mkdir()  # 하위 폴더는 건드리면 안 됨
        (root / "subdir" / "inner.jpg").write_text("x")

        # 중복 케이스: images/a.jpg 가 이미 존재
        (root / "images").mkdir()
        (root / "images" / "a.jpg").write_text("original")

        moved = organize(root)

        assert moved == 4, f"옮긴 파일 수가 4여야 함 (a.jpg는 중복이라 스킵), 실제: {moved}"
        assert (root / "docs" / "b.PDF").exists(), "b.PDF → docs (확장자 대소문자 처리)"
        assert (root / "videos" / "c.mp4").exists(), "c.mp4 → videos"
        assert (root / "etc" / "d.xyz").exists(), "미등록 확장자 → etc"
        assert (root / "archives" / "e.zip").exists(), "e.zip → archives"
        assert (root / "images" / "a.jpg").read_text() == "original", "중복 파일을 덮어쓰면 안 됨"
        assert (root / "a.jpg").exists(), "중복이라 스킵된 원본은 제자리에 남아야 함"
        assert (root / "subdir" / "inner.jpg").exists(), "하위 폴더는 건드리면 안 됨"
    print("PASS ✅ ex1 완료 — 커밋하세요")


if __name__ == "__main__":
    _self_check()
