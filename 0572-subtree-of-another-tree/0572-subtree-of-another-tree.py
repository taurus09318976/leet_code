"""
# 문제핵심: 두 이진 트리가 주어졌을 때, 하나가 다른 하나의 서브트리인지 확인하기

\U0001f50d 코드 이해하기:

1. isSubtree 함수 (메인 로직):
   - root가 None이면 False 반환 (빈 트리에선 찾을 수 없음)
   - 현재 위치에서 완전히 같은 트리인지 확인
   - 같지 않다면 왼쪽, 오른쪽 자식에서 재귀적으로 찾기

2. isSameTree 함수 (보조 로직):
   - 두 트리가 완전히 같은지 확인
   - 구조와 값이 모두 같아야 함
   - 재귀적으로 모든 노드 비교

3. 핵심 아이디어:
   - 큰 트리를 순회하면서 각 노드에서 "여기서 시작하는 서브트리가 찾는 트리와 같나?" 확인
   - OR 연산자로 하나라도 True면 전체가 True

\U0001f914 왜 이렇게 풀까요?
- 서브트리는 어느 노드에서든 시작할 수 있습니다
- 따라서 모든 가능한 시작점을 확인해야 합니다
- 각 시작점에서는 완전히 같은 트리인지 확인하면 됩니다

\U0001f4a1 기억하기 쉬운 방법:
1. "모든 노드에서 시도해보기" (isSubtree)
2. "완전히 같은지 확인하기" (isSameTree)
이 두 가지 기능을 분리해서 생각하세요!
"""


# 1. 먼저 TreeNode 클래스 정의 (이진 트리의 노드를 나타냄)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 노드의 값
        self.left = left    # 왼쪽 자식 노드
        self.right = right  # 오른쪽 자식 노드

class Solution:
    def isSubtree(self, root, subRoot):
        """
        메인 함수: root 트리에서 subRoot와 같은 서브트리가 있는지 확인
        
        Args:
            root: 큰 트리의 루트 노드
            subRoot: 찾고자 하는 서브트리의 루트 노드
            
        Returns:
            bool: 서브트리가 존재하면 True, 없으면 False
        """
        
        # 기본 케이스 1: 큰 트리가 비어있으면 서브트리를 찾을 수 없음
        if not root:
            return False
        
        # 기본 케이스 2: 현재 노드에서 서브트리와 완전히 일치하는지 확인
        if self.isSameTree(root, subRoot):
            return True
        
        # 재귀 케이스: 왼쪽 서브트리 또는 오른쪽 서브트리에서 찾기
        # 왼쪽 서브트리에서 찾거나 OR 오른쪽 서브트리에서 찾으면 True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, tree1, tree2):
        """
        보조 함수: 두 트리가 완전히 같은지 확인 (구조와 값 모두)
        
        Args:
            tree1: 첫 번째 트리의 루트
            tree2: 두 번째 트리의 루트
            
        Returns:
            bool: 두 트리가 같으면 True, 다르면 False
        """
        
        # 기본 케이스 1: 둘 다 비어있으면 같음
        if not tree1 and not tree2:
            return True
        
        # 기본 케이스 2: 하나만 비어있으면 다름
        if not tree1 or not tree2:
            return False
        
        # 기본 케이스 3: 현재 노드의 값이 다르면 다름
        if tree1.val != tree2.val:
            return False
        
        # 재귀 케이스: 왼쪽 서브트리와 오른쪽 서브트리가 모두 같아야 함
        # 왼쪽끼리 같고 AND 오른쪽끼리 같아야 전체가 같음
        return (self.isSameTree(tree1.left, tree2.left) and 
                self.isSameTree(tree1.right, tree2.right))

# ====================================================================
# 문제 이해와 해결 방법 설명
# ====================================================================

"""
\U0001f4da 문제의도:
이 문제는 트리 순회와 재귀적 사고를 연습하는 문제입니다.
- DFS(깊이 우선 탐색) 이해
- 재귀 함수 작성 능력
- 트리 구조 이해

\U0001f3af 해결 방법:
1. 큰 트리의 모든 노드를 순회합니다
2. 각 노드에서 시작하는 서브트리가 찾는 트리와 같은지 확인합니다
3. 같은 트리인지 확인하는 것은 별도 함수로 분리합니다

⏰ 시간복잡도: O(m × n)
- m: root 트리의 노드 개수
- n: subRoot 트리의 노드 개수
- 최악의 경우 root의 모든 노드에서 subRoot와 비교

\U0001f4be 공간복잡도: O(max(m, n))
- 재귀 호출 스택의 깊이는 트리의 높이와 같음
- 균형 트리라면 O(log n), 편향 트리라면 O(n)
"""

# ====================================================================
# 테스트 코드
# ====================================================================

def create_test_tree1():
    """
    테스트용 트리 1 생성:
          3
         / \
        4   5
       / \
      1   2
    """
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    return root

def create_test_tree2():
    """
    테스트용 트리 2 생성:
        4
       / \
      1   2
    """
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    return root

def create_test_tree3():
    """
    테스트용 트리 3 생성:
        4
       / \
      1   2
         /
        0
    """
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(0)
    return root

def run_tests():
    """모든 테스트 실행"""
    solution = Solution()
    
    print("\U0001f9ea 테스트 시작!")
    print("=" * 50)
    
    # 테스트 1: 서브트리가 존재하는 경우
    tree1 = create_test_tree1()
    sub_tree1 = create_test_tree2()
    result1 = solution.isSubtree(tree1, sub_tree1)
    print(f"테스트 1 - 서브트리 존재: {result1}")  # 예상: True
    print("tree1에서 sub_tree1을 찾을 수 있어야 함")
    
    # 테스트 2: 서브트리가 존재하지 않는 경우
    tree2 = create_test_tree1()
    sub_tree2 = create_test_tree3()
    result2 = solution.isSubtree(tree2, sub_tree2)
    print(f"테스트 2 - 서브트리 미존재: {result2}")  # 예상: False
    print("tree2에서 sub_tree2를 찾을 수 없어야 함")
    
    # 테스트 3: 같은 트리인 경우
    tree3 = create_test_tree2()
    sub_tree3 = create_test_tree2()
    result3 = solution.isSubtree(tree3, sub_tree3)
    print(f"테스트 3 - 동일한 트리: {result3}")  # 예상: True
    print("완전히 같은 트리는 서브트리가 맞음")
    
    # 테스트 4: 빈 트리 테스트
    result4 = solution.isSubtree(None, create_test_tree2())
    print(f"테스트 4 - 빈 트리에서 찾기: {result4}")  # 예상: False
    print("빈 트리에서는 어떤 서브트리도 찾을 수 없음")
    
    print("=" * 50)
    print("\U0001f389 모든 테스트 완료!")

# 실제로 테스트 실행
if __name__ == "__main__":
    run_tests()

