# ============================================================
# Day 01 실습용 Dockerfile
# Python 테스트 환경을 컨테이너로 구성
# ============================================================

# 베이스 이미지: Python 3.10 경량 버전
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 먼저 복사 (캐시 활용을 위해)
COPY requirements.txt .

# 의존성 설치
# --no-cache-dir: pip 캐시를 저장하지 않아 이미지 크기 감소
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 기본 실행 명령: pytest로 테스트 실행
CMD ["pytest", "-v", "--tb=short"]
