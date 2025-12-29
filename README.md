# Day 01 실습: Python 기초 함수 구현

## 🎯 이 실습을 완료하면?

이 실습을 통해 다음 역량을 갖추게 됩니다:

| 배우는 것 | 실무 활용 |
|----------|----------|
| `sum()`, `max()`, `min()` | 데이터 집계, 통계 계산 |
| 리스트 컴프리헨션 | 데이터 필터링, 변환 |
| `list.count()`, `dict.fromkeys()` | 데이터 정제, 중복 제거 |
| 문자열 슬라이싱 | 텍스트 데이터 처리 |
| **Docker + Git + GitHub Actions** | CI/CD 파이프라인 기초 |

> 💡 이 실습의 핵심: "코드를 작성하고 → 테스트로 검증하고 → 자동화된 파이프라인으로 배포하는" 현대적인 개발 워크플로우를 경험합니다.

---

## 📚 사전 준비

### 1. Git 설치 확인

터미널에서 다음 명령어를 실행하세요:

```bash
git --version
# 출력 예시: git version 2.39.0
```

설치되지 않았다면: https://git-scm.com/downloads

### 2. Docker Desktop 설치

터미널에서 다음 명령어를 실행하세요:

```bash
docker --version
# 출력 예시: Docker version 24.0.0
```

설치되지 않았다면: https://www.docker.com/products/docker-desktop

> ⚠️ **중요**: Docker Desktop이 **실행 중**이어야 합니다! (시스템 트레이에서 고래 아이콘 확인)

### 3. GitHub 계정

GitHub 계정이 없다면: https://github.com/signup

---

## 🚀 Step by Step 실습 가이드

### Step 1: 저장소 Fork하기

1. GitHub에서 이 저장소 페이지로 이동
2. 오른쪽 상단의 **Fork** 버튼 클릭
3. "Create fork" 클릭
4. 이제 `https://github.com/YOUR_USERNAME/day01-python-exercise`가 생성됨

> 🔍 **Fork란?** 다른 사람의 저장소를 내 계정으로 복사하는 것. 원본에 영향을 주지 않고 자유롭게 수정 가능.

### Step 2: 로컬에 Clone하기

```bash
# YOUR_USERNAME을 본인의 GitHub 사용자명으로 변경
git clone https://github.com/YOUR_USERNAME/day01-python-exercise.git

# 폴더로 이동
cd day01-python-exercise
```

> 🔍 **Clone이란?** GitHub에 있는 저장소를 내 컴퓨터로 다운로드하는 것.

### Step 3: 현재 상태 확인 (모든 테스트 실패!)

```bash
docker compose run --rm test
```

47개 테스트가 모두 **FAILED**로 나오는 것이 정상입니다! 아직 코드를 작성하지 않았기 때문이죠.

### Step 4: 첫 번째 함수 구현하기

`exercise.py` 파일을 에디터로 열고, 첫 번째 함수를 구현합니다:

```python
def calculate_sum(numbers: list) -> int | float:
    # TODO: 여기에 코드를 작성하세요
    return sum(numbers)  # ← 이렇게 수정!
```

### Step 5: 특정 테스트만 실행하기

전체 47개를 돌리지 않고, 방금 구현한 함수만 테스트합니다:

```bash
docker compose run --rm test pytest test_exercise.py::TestCalculateSum -v
```

✅ **5 passed**가 나오면 성공!

### Step 6: 나머지 함수들도 구현하기

같은 방식으로 나머지 함수들을 하나씩 구현합니다:

| 순서 | 함수명 | 테스트 명령어 |
|------|--------|-------------|
| 1 | `calculate_sum` | `pytest test_exercise.py::TestCalculateSum -v` |
| 2 | `find_max` | `pytest test_exercise.py::TestFindMax -v` |
| 3 | `find_min` | `pytest test_exercise.py::TestFindMin -v` |
| 4 | `calculate_average` | `pytest test_exercise.py::TestCalculateAverage -v` |
| 5 | `filter_even` | `pytest test_exercise.py::TestFilterEven -v` |
| 6 | `filter_odd` | `pytest test_exercise.py::TestFilterOdd -v` |
| 7 | `count_occurrences` | `pytest test_exercise.py::TestCountOccurrences -v` |
| 8 | `remove_duplicates` | `pytest test_exercise.py::TestRemoveDuplicates -v` |
| 9 | `reverse_string` | `pytest test_exercise.py::TestReverseString -v` |
| 10 | `is_palindrome` | `pytest test_exercise.py::TestIsPalindrome -v` |

> 💡 테스트 명령어 앞에 `docker compose run --rm test`를 붙여서 실행하세요!

### Step 7: 전체 테스트 통과 확인

모든 함수를 구현했다면:

```bash
docker compose run --rm test
```

**47 passed**가 나오면 성공!

### Step 8: GitHub에 Push하기

```bash
# 변경사항 확인
git status

# 모든 변경사항 스테이징
git add .

# 커밋 메시지 작성
git commit -m "feat: 모든 함수 구현 완료"

# GitHub에 업로드
git push origin main
```

### Step 9: GitHub Actions 확인하기

1. GitHub에서 본인의 저장소로 이동
2. **Actions** 탭 클릭
3. 녹색 체크마크(✅)가 보이면 **실습 완료!**

---

## 💡 막혔을 때는?

각 단계별로 정답이 포함된 브랜치가 준비되어 있습니다:

| 브랜치 | 포함된 함수 |
|--------|-----------|
| `base` | 빈칸 상태 (시작점) |
| `step-1` | calculate_sum, find_max, find_min |
| `step-2` | + calculate_average |
| `step-3` | + filter_even, filter_odd |
| `step-4` | + count_occurrences, remove_duplicates |
| `step-5` | + reverse_string, is_palindrome |
| `main` | 모든 함수 완성 |

### 정답 확인 방법

```bash
# step-1에서 추가된 코드 확인
git diff base step-1 -- exercise.py

# 또는 해당 브랜치로 전환해서 코드 확인
git checkout step-1
cat exercise.py

# 다시 원래 브랜치로 돌아오기
git checkout main
```

---

## 🐳 Docker 명령어 모음

| 명령어 | 설명 |
|--------|------|
| `docker compose run --rm test` | 전체 테스트 실행 |
| `docker compose run --rm test pytest test_exercise.py::TestXXX -v` | 특정 테스트만 실행 |
| `docker compose run --rm shell` | Python 대화형 셸 (디버깅용) |
| `docker compose build --no-cache` | 이미지 다시 빌드 |

---

## ⚠️ 자주 발생하는 오류

### "docker: command not found"

**원인**: Docker가 설치되지 않았거나 실행 중이 아님

**해결**:
1. Docker Desktop 설치: https://www.docker.com/products/docker-desktop
2. Docker Desktop이 실행 중인지 확인 (시스템 트레이 고래 아이콘)

### "Cannot connect to the Docker daemon"

**원인**: Docker Desktop이 실행 중이 아님

**해결**: Docker Desktop을 실행하세요

### "docker compose: command not found"

**원인**: Docker 버전이 오래됨

**해결**:
- Docker Desktop을 최신 버전으로 업데이트
- 또는 `docker-compose` (하이픈 포함) 시도

### 테스트가 전부 실패함

**원인**: 정상! 아직 코드를 작성하지 않았기 때문

**해결**: Step 4부터 차근차근 함수를 구현하세요

### "assert None == 6" 같은 에러

**원인**: 함수에서 `return`이 빠졌거나 `pass`가 남아있음

**해결**: 함수가 값을 반환하는지 확인

```python
# ❌ 잘못된 예
def calculate_sum(numbers):
    sum(numbers)  # return이 없음!

# ✅ 올바른 예
def calculate_sum(numbers):
    return sum(numbers)
```

---

## 📁 파일 구조

```
day01-python-exercise/
├── README.md              # 이 파일 (실습 가이드)
├── exercise.py            # 🎯 빈칸 채우기 대상
├── test_exercise.py       # 테스트 코드 (수정 금지)
├── requirements.txt       # Python 패키지 목록
├── Dockerfile             # Docker 이미지 설정
├── docker-compose.yml     # Docker 서비스 설정
├── .dockerignore          # Docker 빌드 제외 파일
├── .gitignore             # Git 무시 파일
└── .github/
    └── workflows/
        └── test.yml       # GitHub Actions 설정
```

---

## 🎉 실습 완료 체크리스트

- [ ] 모든 47개 테스트 통과 (`docker compose run --rm test`)
- [ ] GitHub에 Push 완료 (`git push origin main`)
- [ ] GitHub Actions에서 녹색 체크마크(✅) 확인

**수고하셨습니다!** 🚀
