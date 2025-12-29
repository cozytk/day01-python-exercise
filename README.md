# Day 01 실습: 환경 구축 및 Python 기초

## 개요

이 실습에서는 다음을 학습합니다:
- Python 기초 함수 구현
- Docker를 활용한 테스트 환경 구성
- Unit Test 작성 및 실행 방법
- GitHub Actions 자동 테스트 체험

## 실습 흐름

```
┌─────────────────────────────────────────────────────────────┐
│  1. 저장소 Fork & Clone                                     │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  2. exercise.py 빈칸 채우기 (TODO 부분 작성)                  │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  3. 로컬 Docker에서 테스트                                   │
│     $ docker-compose run --rm test                          │
└─────────────────────────────────────────────────────────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
           ✅ 통과               ❌ 실패
                 │                   │
                 │                   └── 코드 수정 후 다시 테스트
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  4. GitHub에 Push                                           │
│     $ git add . && git commit -m "feat: 실습 완료"           │
│     $ git push                                              │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  5. GitHub Actions 자동 테스트 확인                          │
│     → Actions 탭에서 ✅ 확인하면 완료!                       │
└─────────────────────────────────────────────────────────────┘
```

## 실습 방법

### 방법 1: Docker 사용 (권장) ⭐

패키지 설치 없이 바로 테스트할 수 있습니다.

```bash
# 1. 저장소 Clone
git clone https://github.com/YOUR_USERNAME/day01-exercise.git
cd day01-exercise

# 2. exercise.py 빈칸 채우기 (에디터로 열어서 TODO 부분 작성)

# 3. Docker로 테스트 실행
docker-compose run --rm test

# 4. 테스트 통과하면 Push
git add .
git commit -m "feat: 실습 완료"
git push
```

### 방법 2: 로컬 Python 사용

```bash
# 1. 저장소 Clone
git clone https://github.com/YOUR_USERNAME/day01-exercise.git
cd day01-exercise

# 2. 의존성 설치
pip install -r requirements.txt

# 3. exercise.py 빈칸 채우기

# 4. 테스트 실행
pytest -v

# 5. 테스트 통과하면 Push
git add .
git commit -m "feat: 실습 완료"
git push
```

## Docker 명령어

| 명령어 | 설명 |
|--------|------|
| `docker-compose run --rm test` | 전체 테스트 실행 |
| `docker-compose run --rm shell` | Python 대화형 셸 (디버깅용) |
| `docker-compose build` | 이미지 다시 빌드 |

## 파일 구조

```
Day01_실습/
├── README.md              # 이 파일
├── exercise.py            # 빈칸 채우기 대상 파일 ⭐
├── test_exercise.py       # 테스트 코드 (수정 금지)
├── requirements.txt       # 의존성 패키지
├── Dockerfile             # 테스트 환경 이미지 정의
├── docker-compose.yml     # 테스트 서비스 정의
├── .dockerignore          # Docker 빌드 제외 파일
├── .gitignore             # Git 무시 파일
└── .github/
    └── workflows/
        └── test.yml       # GitHub Actions 설정
```

## 채점 기준

- 모든 테스트 케이스 통과 시 ✅ 완료
- 테스트 실패 시 힌트를 참고하여 수정

## 힌트

각 함수의 docstring에 힌트가 포함되어 있습니다.
막히는 부분이 있으면 테스트 코드(`test_exercise.py`)를 참고하세요.

## 트러블슈팅

### Docker 관련

| 문제 | 해결 방법 |
|------|----------|
| `docker-compose: command not found` | Docker Desktop 설치 확인 |
| 이미지 빌드 실패 | `docker-compose build --no-cache` |
| 권한 오류 | `sudo` 추가 또는 Docker 그룹 설정 |

### 테스트 관련

| 문제 | 해결 방법 |
|------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| 특정 테스트만 실행하고 싶음 | `pytest test_exercise.py::TestCalculateSum -v` |
