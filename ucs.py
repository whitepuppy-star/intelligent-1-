import heapq

def uniform_cost_search(problem):
    """최소 비용을 가진 노드를 우선적으로 탐색한다."""
    
    # 1. 초기화: (누적 비용, 현재 상태, 행동 리스트)를 큐에 넣는다.
    # heapq는 첫 번째 요소인 '비용'을 기준으로 최소값을 자동으로 유지한다.
    start_state = problem.getStartState()
    # (cost, state, path)
    queue = [(0, start_state, [])]
    
    # 이미 방문한 노드를 기록하여 O(1) 시간 복잡도로 중복을 방지한다.
    visited = set()
    expanded_nodes = 0

    while queue:
        # 2. 우선순위 큐에서 비용이 가장 적은 노드를 꺼낸다. (queue.get() 역할)
        current_cost, current_state, actions = heapq.heappop(queue)

        # 3. 이미 방문한 노드라면 건너뛴다. (if current not in visited 로직)
        if current_state in visited:
            continue
            
        # 4. 방문 처리 및 확장 노드 카운트
        visited.add(current_state)
        expanded_nodes += 1

        # 5. 목표 상태 도달 확인 (이미지의 dest 체크 로직)
        if problem.isGoalState(current_state):
            return actions, len(actions), expanded_nodes

        # 6. 현재 노드의 자식 노드들을 생성하고 확장한다. (current.expand 역할)
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in visited:
                # 누적 가중치 합 계산: 부모의 비용 + 현재 이동 비용
                new_cost = current_cost + step_cost
                new_actions = actions + [action]
                
                # 7. 큐에 새로운 상태를 추가한다. (queue.put 역할)
                heapq.heappush(queue, (new_cost, next_state, new_actions))

    # 탐색 실패 시
    return [], 0, expanded_nodes
