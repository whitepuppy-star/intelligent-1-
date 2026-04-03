import heapq

def a_star_search(problem, heuristic):
    # 1. 초기 설정
    start_state = problem.getStartState()
    count = 0
    # 큐 구성: (f_score, count, 현재_상태, 현재까지_경로, g_score)
    # f(n) = g(n) + h(n)
    g_score = 0
    h_score = heuristic(start_state, problem)
    f_score = g_score + h_score
    
    queue = [(f_score, count, start_state, [], g_score)]
    visited = set()
    expanded_nodes = 0

    while queue:
        # 2. f_score(우선순위)가 가장 낮은 노드를 꺼낸다
        current_f, _, current_state, actions, current_g = heapq.heappop(queue)

        if current_state in visited:
            continue
        
        visited.add(current_state)
        expanded_nodes += 1

        # 3. 목표 도달 확인
        if problem.isGoalState(current_state):
            return actions, len(actions), expanded_nodes

        # 4. 인접 노드(자식) 확장
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in visited:
                # g(n): 시작부터 다음 노드까지의 실제 비용
                next_g = current_g + step_cost
                # h(n): 다음 노드에서 목표까지의 예상 비용 (휴리스틱)
                next_h = heuristic(next_state, problem)
                # f(n) = g(n) + h(n)
                next_f = next_g + next_h
                
                count += 1
                heapq.heappush(queue, (next_f, count, next_state, actions + [action], next_g))

    return [], 0, expanded_nodes
