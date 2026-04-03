def breadth_first_search(problem):
    """너비 우선 탐색을 수행하여 최단 경로를 찾습니다."""
    
    # 1. 시작 상태 설정
    start_state = problem.getStartState()
    
    # 시작 상태가 이미 목표 상태인지 확인
    if problem.isGoalState(start_state):
        return [], 0, 0

    # 2. 자료구조 초기화
    # 큐에는 (현재_상태, 여기까지의_행동_리스트) 튜플을 저장합니다.
    queue = deque([(start_state, [])])
    
    # 이미 방문한 상태를 기록 (중복 탐색 방지)
    visited = set()
    visited.add(start_state)
    
    expanded_nodes = 0

    # 3. 탐색 시작
    while queue:
        current_state, actions = queue.popleft()
        
        # 노드를 확장함 (getSuccessors 호출 시점을 확장으로 간주)
        expanded_nodes += 1
        
        # 현재 상태에서 갈 수 있는 다음 상태들 가져오기
        successors = problem.getSuccessors(current_state)
        
        for next_state, action, cost in successors:
            if next_state not in visited:
                # 새로운 경로 생성
                new_actions = actions + [action]
                
                # 목표 상태 도달 확인 (목표 검사 - Goal Test)
                if problem.isGoalState(next_state):
                    # 결과 반환: (경로 리스트, 총 비용, 확장된 노드 수)
                    # 8-퍼즐에서 비용은 보통 경로의 길이와 같습니다.
                    return new_actions, len(new_actions), expanded_nodes
                
                # 방문 표시 및 큐에 추가
                visited.add(next_state)
                queue.append((next_state, new_actions))

    # 탐색 실패 시
    return [], 0, expanded_nodes
