class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 보드의 행과 열 수
        rows, cols = len(board), len(board[0])
        # 방문한 셀을 추적하는 집합
        visited = set()
        
        # DFS 함수 정의
        def dfs(r, c, i):
            # 단어의 모든 문자를 찾은 경우
            if i == len(word):
                return True
            
            # 범위를 벗어나거나 이미 방문했거나 문자가 일치하지 않는 경우
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                (r, c) in visited or 
                board[r][c] != word[i]):
                return False
            
            # 현재 셀을 방문했다고 표시
            visited.add((r, c))
            
            # 상하좌우 방향으로 탐색
            result = (dfs(r + 1, c, i + 1) or  # 아래
                     dfs(r - 1, c, i + 1) or  # 위
                     dfs(r, c + 1, i + 1) or  # 오른쪽
                     dfs(r, c - 1, i + 1))    # 왼쪽
            
            # 백트래킹: 현재 셀을 방문하지 않은 것으로 표시
            visited.remove((r, c))
            
            return result
        
        # 보드의 모든 셀에서 시작점으로 시도
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
        


        #시간 복잡도 (Time Complexity): O(m * n * 4^L)
            #m: 보드의 행 수
            #n: 보드의 열 수
            #L: 단어의 길이
            #이유:
                #각 셀에서 시작할 수 있음: O(m * n)
                #각 위치에서 4방향으로 탐색 가능: O(4^L)
                #최악의 경우 모든 경로를 탐색해야 함
                #따라서 시간 복잡도는 O(m * n * 4^L)
        #공간 복잡도 (Space Complexity): O(L)
            #L: 단어의 길이
            #이유:
                #재귀 호출 스택의 깊이는 단어의 길이에 비례
                #visited 집합의 크기도 단어의 길이에 비례
                #따라서 공간 복잡도는 O(L)
        #DFS vs BFS 비교:
            #DFS (깊이 우선 탐색):
            #한 경로를 끝까지 탐색
            #스택/재귀 사용
            #메모리 사용이 적음
            #최단 경로 보장하지 않음
        #BFS (너비 우선 탐색):
            #같은 레벨의 모든 노드를 먼저 탐색
            #큐 사용
            #메모리 사용이 많음
            #최단 경로 보장