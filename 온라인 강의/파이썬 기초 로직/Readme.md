# 🐍 Python Basic Logic Implementation

파이썬의 핵심 내장 함수와 효율적인 알고리즘 구조를 활용하여 실무에서 자주 쓰이는 5가지 로직을 구현한 연습 저장소입니다.

## 📝 구현 목록 (Task List)

1. **공백 정규화 (`normalize_ws`)**
   - 연속된 공백(Space, Tab, Newline)을 단일 공백으로 축약하고 앞뒤 공백을 제거합니다.
   - 활용: 문자열 슬라이싱, `split()`, `join()`

2. **순서 유지 중복 제거 (`unique_keep_order`)**
   - 요소의 첫 등장 순서를 보존하면서 중복을 제거합니다.
   - 활용: `dict` 또는 `set`을 이용한 $O(N)$ 시간 복잡도 구현

3. **괄호 유효성 검사 (`is_valid_brackets`)**
   - `()`, `[]`, `{}` 괄호 쌍이 올바르게 닫혔는지 확인합니다.
   - 활용: **Stack(LIFO)** 자료구조 및 매핑 테이블 활용

4. **쿼리 스트링 파싱 (`parse_query`)**
   - URL 형태의 쿼리 스트링을 파이썬 딕셔너리(`dict[str, list[str]]`)로 변환합니다.
   - 활용: 문자열 파싱, Key-Value 리스트 구조 관리

5. **정렬된 리스트 병합 (`merge_sorted`)**
   - 이미 정렬된 두 리스트를 `sort()` 함수 없이 하나로 합칩니다.
   - 활용: **Two-Pointers** 알고리즘 기반 $O(N + M)$ 최적화

## 🚀 실행 방법 (Test)

본 프로젝트는 `pytest`를 기반으로 작성되었습니다.

```bash
# pytest 설치 (없을 경우)
pip install pytest

# 테스트 실행
python -m pytest -v