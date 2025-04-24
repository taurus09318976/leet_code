# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

# 연결 리스트의 노드를 정의하는 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        # 노드의 값
        self.val = val
        # 다음 노드를 가리키는 포인터 
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        # 더미 노드 생성 - 결과 리스트의 시작점으로 사용
        dummy = ListNode()
        # 현재 위치를 추적하는 포인터
        current = dummy
        
        # 두 리스트가 모두 존재하는 동안 반복
        while list1 and list2:
            # list 1의 값이 list2의 값보다 작거나 같은 경우
            if list1.val <= list2.val:
                # list1의 노드를 결과에 추가
                current.next = list1
                #list1의 포인터를 다음 노드로 이동
                list1 = list1.next
            else:
                #list2의 노드를 결과에 추가
                current.next = list2
                #list2의 포인터를 다음 노드로 이동
                list2 = list2.next
                #결과 리스트의 포인터를 다음으로 이동
            current = current.next
        
        # 남은 노드들 연결
        ## list1에 남은 노드가 있으면 모두 연결
        if list1:
            current.next = list1
        
        ## list2에 남은 노드가 있으면 모두 연결
        else:
            current.next = list2

        # 더미 노드의 다음 노드부터가 실제 결과    
        return dummy.next

# 리스트를 연결 리스트로 변환하는 헬퍼 함수
def create_linked_list(lst):
    #빈 리스트인 경우
    if not lst:
        return None
    #첫번째 노드 생성
    head = ListNode(lst[0])
    #현재 노드를 추적하는 포인터
    current = head
    for val in lst[1:]:
        ##나머지 값들에 대해 새 노드 생성 후 연결 
        current.next = ListNode(val)
        ##포인터 이동
        current = current.next
    # 연결 리스트의 헤드 반환    
    return head

#연결 리스트를 리스트로 변환하는 헬퍼 함수
def linked_list_to_list(head):
    #결과를 저장할 리스트
    result = []
    #연결 리스트의 끝까지 현재 노드의 값을 결과에 추가
    while head:
        result.append(head.val)
        ##다음 노드로 이동
        head = head.next
    #변환된 리스트 반환
    return result


# 테스트 코드
solution = Solution()

# 테스트 케이스 1: [1,2,4]와 [1,3,4] 병합
list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])
result = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(result))  
# [1,1,2,3,4,4] 출력

# 테스트 케이스 2: 빈 리스트 두 개 병합
list1 = create_linked_list([])
list2 = create_linked_list([])
result = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(result))  
# [] 출력

# 테스트 케이스 3: 빈 리스트와 [0] 병합
list1 = create_linked_list([])
list2 = create_linked_list([0])
result = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(result)) 
# [0] 출력