"""
Day 01 실습: Python 기초 함수 구현

이 파일의 TODO 부분을 완성하세요.
각 함수의 docstring에 힌트와 예시가 포함되어 있습니다.
"""


def calculate_sum(numbers: list) -> int | float:
    """
    리스트의 합계를 계산합니다.

    Args:
        numbers: 숫자 리스트

    Returns:
        int or float: 합계

    Example:
        >>> calculate_sum([1, 2, 3])
        6
        >>> calculate_sum([])
        0

    힌트: sum() 내장 함수를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def find_max(numbers: list) -> int | float:
    """
    리스트에서 최댓값을 찾습니다.

    Args:
        numbers: 숫자 리스트 (비어있지 않음)

    Returns:
        int or float: 최댓값

    Example:
        >>> find_max([1, 5, 3])
        5
        >>> find_max([-10, -5, -1])
        -1

    힌트: max() 내장 함수를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def find_min(numbers: list) -> int | float:
    """
    리스트에서 최솟값을 찾습니다.

    Args:
        numbers: 숫자 리스트 (비어있지 않음)

    Returns:
        int or float: 최솟값

    Example:
        >>> find_min([1, 5, 3])
        1
        >>> find_min([-10, -5, -1])
        -10

    힌트: min() 내장 함수를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def calculate_average(numbers: list) -> float:
    """
    리스트의 평균을 계산합니다.

    Args:
        numbers: 숫자 리스트 (비어있지 않음)

    Returns:
        float: 평균값

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10, 20])
        15.0

    힌트: sum()과 len() 함수를 조합하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def filter_even(numbers: list) -> list:
    """
    리스트에서 짝수만 필터링합니다.

    Args:
        numbers: 숫자 리스트

    Returns:
        list: 짝수만 포함된 리스트

    Example:
        >>> filter_even([1, 2, 3, 4, 5])
        [2, 4]
        >>> filter_even([1, 3, 5])
        []

    힌트: 리스트 컴프리헨션과 % 연산자를 사용하세요
          n % 2 == 0 이면 짝수입니다
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def filter_odd(numbers: list) -> list:
    """
    리스트에서 홀수만 필터링합니다.

    Args:
        numbers: 숫자 리스트

    Returns:
        list: 홀수만 포함된 리스트

    Example:
        >>> filter_odd([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> filter_odd([2, 4, 6])
        []

    힌트: 리스트 컴프리헨션과 % 연산자를 사용하세요
          n % 2 != 0 이면 홀수입니다
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def count_occurrences(items: list, target) -> int:
    """
    리스트에서 특정 값의 등장 횟수를 셉니다.

    Args:
        items: 리스트
        target: 찾을 값

    Returns:
        int: 등장 횟수

    Example:
        >>> count_occurrences([1, 2, 2, 3, 2], 2)
        3
        >>> count_occurrences(['a', 'b', 'a'], 'a')
        2

    힌트: list.count() 메서드를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def remove_duplicates(items: list) -> list:
    """
    리스트에서 중복을 제거합니다. (순서 유지)

    Args:
        items: 리스트

    Returns:
        list: 중복이 제거된 리스트

    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1])
        [1, 2, 3]
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']

    힌트: dict.fromkeys()를 사용하면 순서를 유지하면서 중복 제거 가능
          list(dict.fromkeys(items))
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def reverse_string(text: str) -> str:
    """
    문자열을 뒤집습니다.

    Args:
        text: 문자열

    Returns:
        str: 뒤집힌 문자열

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'

    힌트: 슬라이싱 [::-1]을 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def is_palindrome(text: str) -> bool:
    """
    문자열이 회문(팰린드롬)인지 확인합니다.
    (앞에서 읽어도 뒤에서 읽어도 같은 문자열)

    Args:
        text: 문자열

    Returns:
        bool: 회문이면 True

    Example:
        >>> is_palindrome("radar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("level")
        True

    힌트: 문자열과 뒤집은 문자열을 비교하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass
