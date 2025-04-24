#이 문제를 해결하기 위해선 Counter 함수를 쓰는 것이 가장 파이썬다운 풀이방식임 
class Solution:
    def isAnagram(self, s: str, t: str):
        # 두 문자열의 길이가 다르면 아나그램이 될 수 없음
        return Counter(s) == Counter(t)

        #시간 복잡도: O(n), n= 문자열의 길이
        #공간 복잡도: O(1), 입력 크기(n)가 아무리 커져도 사용하는 공간이 일정함(영어 소문자만 사용하므로 최대 26개의 키만 저장하면 됨)