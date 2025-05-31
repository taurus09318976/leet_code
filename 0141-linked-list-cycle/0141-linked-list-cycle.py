'''
문제의 의도 : 
이 문제는 연결 리스트에 사이클이 있는지 판단하는 문제임. 
사이클이란 어떤 노드에서 시작해서 next 포인터를 계속 이동시키다 다시 원래 노드로 돌아올 수 있는 경우를 말함

해결방법 : 토끼와 거북이 알고리듬을 사용함
두 개의 포인터를 사용하는데, 느린 포인터(거북이)는 한 번에 한칸씩 이동,
빠른 포인터(토끼)는 한 번에 두 칸씩 이동, 사이클이 존재한다면 빠른 포인터가 느린 포인터를 따라잡게 됨.

'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 연결 리스트가 비어 있거나 노드가 하나뿐이면 사이클이 불가능하므로 False 반환
        if not head or not head.next:
            return False
        
        # 두 포인터를 모두 head에서 시작하도록 초기화
        slow = head      # 느린 포인터 (거북이)
        fast = head      # 빠른 포인터 (토끼)
        
        # 빠른 포인터가 두 칸씩 이동하므로, fast와 fast.next 모두 존재하는지 확인
        while fast and fast.next:
            slow = slow.next        # 느린 포인터는 한 칸씩 이동
            fast = fast.next.next   # 빠른 포인터는 두 칸씩 이동
            
            # 두 포인터가 같은 노드를 가리키면 사이클이 존재함을 의미
            if slow == fast:
                return True
        
        # 빠른 포인터가 끝에 도달하면 사이클이 없다는 의미
        return False
