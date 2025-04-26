class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 배열의 시작과 끝 인덱스 설정
        left, right = 0, len(nums) - 1
        
        # 배열이 회전되지 않은 경우 (첫 번째 요소가 최소값)
        if nums[left] < nums[right]:
            return nums[left]
        
        # 이진 탐색 실행
        while left < right:
            # 중간 인덱스 계산
            mid = (left + right) // 2
            
            # 중간값이 오른쪽 값보다 큰 경우
            # -> 최소값은 중간값 오른쪽에 있음
            if nums[mid] > nums[right]:
                left = mid + 1
            # 중간값이 오른쪽 값보다 작거나 같은 경우
            # -> 최소값은 중간값 포함 왼쪽에 있음
            else:
                right = mid
        
        # 최소값 반환
        return nums[left]

# 테스트 코드
print(Solution().findMin([3, 4, 5, 1, 2]))  # 출력: 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # 출력: 0
print(Solution().findMin([1]))  # 출력: 1