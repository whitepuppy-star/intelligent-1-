def heuristic(state, problem=None):
    # Misplaced Tiles: 현재 타일과 목표 상태를 비교해 정답 자리에 없는 타일의 개수를 센다.
    misplaced = 0
    cells = state.cells
    
    # 정답 (1, 2, 3, 4, 5, 6, 7, 8, 0)
    goal_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    idx = 0
    
    for r in range(3):
        for c in range(3):
            target = goal_pattern[idx]  # 이 자리에 있어야 할 숫자
            current_val = cells[r][c]   # 지금 이 자리에 있는 숫자
            
            # 빈 칸(0)은 개수에서 제외
            if current_val != 0:
                # 현재 타일이 목표 위치의 타일과 다르면 count 하기.
                if current_val != target:
                    misplaced += 1
            
            # 다음 칸으로 넘어가기 위해 인덱스 증가 
            idx += 1
            
    return misplaced    
