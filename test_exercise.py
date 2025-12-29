"""
Day 01 실습 테스트

이 파일은 exercise.py의 함수들을 테스트합니다.
수정하지 마세요!
"""
import pytest
from exercise import (
    calculate_sum,
    find_max,
    find_min,
    calculate_average,
    filter_even,
    filter_odd,
    count_occurrences,
    remove_duplicates,
    reverse_string,
    is_palindrome,
)


class TestCalculateSum:
    """calculate_sum 함수 테스트"""

    def test_positive_numbers(self):
        """양수 리스트의 합계"""
        assert calculate_sum([1, 2, 3]) == 6

    def test_negative_numbers(self):
        """음수 리스트의 합계"""
        assert calculate_sum([-1, -2, -3]) == -6

    def test_mixed_numbers(self):
        """양수와 음수가 섞인 리스트"""
        assert calculate_sum([1, -1, 2, -2]) == 0

    def test_empty_list(self):
        """빈 리스트"""
        assert calculate_sum([]) == 0

    def test_single_element(self):
        """단일 요소"""
        assert calculate_sum([42]) == 42


class TestFindMax:
    """find_max 함수 테스트"""

    def test_positive_numbers(self):
        """양수 리스트에서 최댓값"""
        assert find_max([1, 5, 3]) == 5

    def test_negative_numbers(self):
        """음수 리스트에서 최댓값"""
        assert find_max([-5, -1, -3]) == -1

    def test_single_element(self):
        """단일 요소"""
        assert find_max([42]) == 42

    def test_duplicates(self):
        """중복 요소 포함"""
        assert find_max([3, 3, 3]) == 3


class TestFindMin:
    """find_min 함수 테스트"""

    def test_positive_numbers(self):
        """양수 리스트에서 최솟값"""
        assert find_min([1, 5, 3]) == 1

    def test_negative_numbers(self):
        """음수 리스트에서 최솟값"""
        assert find_min([-5, -1, -3]) == -5

    def test_single_element(self):
        """단일 요소"""
        assert find_min([42]) == 42


class TestCalculateAverage:
    """calculate_average 함수 테스트"""

    def test_integer_average(self):
        """정수 평균"""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0

    def test_two_numbers(self):
        """두 숫자 평균"""
        assert calculate_average([10, 20]) == 15.0

    def test_single_number(self):
        """단일 숫자"""
        assert calculate_average([5]) == 5.0

    def test_float_result(self):
        """소수점 결과"""
        assert calculate_average([1, 2]) == 1.5


class TestFilterEven:
    """filter_even 함수 테스트"""

    def test_mixed_numbers(self):
        """짝수와 홀수가 섞인 리스트"""
        assert filter_even([1, 2, 3, 4, 5]) == [2, 4]

    def test_all_odd(self):
        """모두 홀수"""
        assert filter_even([1, 3, 5]) == []

    def test_all_even(self):
        """모두 짝수"""
        assert filter_even([2, 4, 6]) == [2, 4, 6]

    def test_empty_list(self):
        """빈 리스트"""
        assert filter_even([]) == []

    def test_with_zero(self):
        """0 포함 (0은 짝수)"""
        assert filter_even([0, 1, 2]) == [0, 2]


class TestFilterOdd:
    """filter_odd 함수 테스트"""

    def test_mixed_numbers(self):
        """짝수와 홀수가 섞인 리스트"""
        assert filter_odd([1, 2, 3, 4, 5]) == [1, 3, 5]

    def test_all_even(self):
        """모두 짝수"""
        assert filter_odd([2, 4, 6]) == []

    def test_all_odd(self):
        """모두 홀수"""
        assert filter_odd([1, 3, 5]) == [1, 3, 5]

    def test_empty_list(self):
        """빈 리스트"""
        assert filter_odd([]) == []


class TestCountOccurrences:
    """count_occurrences 함수 테스트"""

    def test_multiple_occurrences(self):
        """여러 번 등장"""
        assert count_occurrences([1, 2, 2, 3, 2], 2) == 3

    def test_single_occurrence(self):
        """한 번 등장"""
        assert count_occurrences([1, 2, 3], 1) == 1

    def test_no_occurrence(self):
        """등장하지 않음"""
        assert count_occurrences([1, 2, 3], 5) == 0

    def test_string_items(self):
        """문자열 리스트"""
        assert count_occurrences(["a", "b", "a"], "a") == 2

    def test_empty_list(self):
        """빈 리스트"""
        assert count_occurrences([], 1) == 0


class TestRemoveDuplicates:
    """remove_duplicates 함수 테스트"""

    def test_with_duplicates(self):
        """중복 있는 리스트"""
        assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]

    def test_no_duplicates(self):
        """중복 없는 리스트"""
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_all_same(self):
        """모두 같은 값"""
        assert remove_duplicates([5, 5, 5]) == [5]

    def test_string_items(self):
        """문자열 리스트"""
        assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]

    def test_empty_list(self):
        """빈 리스트"""
        assert remove_duplicates([]) == []


class TestReverseString:
    """reverse_string 함수 테스트"""

    def test_simple_word(self):
        """간단한 단어"""
        assert reverse_string("hello") == "olleh"

    def test_capitalized(self):
        """대문자 포함"""
        assert reverse_string("Python") == "nohtyP"

    def test_single_char(self):
        """단일 문자"""
        assert reverse_string("a") == "a"

    def test_empty_string(self):
        """빈 문자열"""
        assert reverse_string("") == ""

    def test_with_spaces(self):
        """공백 포함"""
        assert reverse_string("a b c") == "c b a"


class TestIsPalindrome:
    """is_palindrome 함수 테스트"""

    def test_palindrome_radar(self):
        """회문: radar"""
        assert is_palindrome("radar") is True

    def test_palindrome_level(self):
        """회문: level"""
        assert is_palindrome("level") is True

    def test_not_palindrome(self):
        """회문 아님: hello"""
        assert is_palindrome("hello") is False

    def test_single_char(self):
        """단일 문자 (회문)"""
        assert is_palindrome("a") is True

    def test_empty_string(self):
        """빈 문자열 (회문)"""
        assert is_palindrome("") is True

    def test_two_same_chars(self):
        """같은 두 문자 (회문)"""
        assert is_palindrome("aa") is True

    def test_two_different_chars(self):
        """다른 두 문자 (회문 아님)"""
        assert is_palindrome("ab") is False
