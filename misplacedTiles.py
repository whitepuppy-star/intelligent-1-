def misplaced_heuristic(state, problem):
    """
    현재 상태와 목표 상태를 비교하여 위치가 틀린 타일의 개수를 반환한다.
    (단, 빈 칸인 0은 제외한다.)
    """
    misplaced = 0
    # 현재 퍼즐 상태 (예: ((1, 2, 3), (4, 8, 0), (7, 6, 5)))
    current_cells = state.cells 
    # 목표 퍼즐 상태
    goal_cells = problem.goal.cells

    for r in range(3):
        for c in range(3):
            # 1. 빈 칸(0)이 아닌 타일에 대해서만 검사한다.
            if current_cells[r][c] != 0:
                # 2. 현재 타일이 목표 위치의 타일과 다르면 카운트한다.
                if current_cells[r][c] != goal_cells[r][c]:
                    misplaced += 1
                    
    return misplaced
