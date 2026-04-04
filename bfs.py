def breadth_first_search(problem):
    # 1. 초기 설정 
    StartNode = problem.getStartState()
    # 방문 기록부 (중복 방지용 set)
    Visited = set()
    # 탐색 대기소 (BFS이므로 deque 사용)
    Queue = deque([(StartNode, [])])
    
    # 시작 노드를 넣자마자 방문 처리 
    Visited.add(StartNode)
    ExpandedNodeCount = 0

    while Queue:
        # 2. 큐의 맨 앞(왼쪽)에서 데이터를 꺼냄
        CurrentState, Actions = Queue.popleft()
        ExpandedNodeCount += 1 

        # 3. 목표 상태(정답)인지 확인
        if problem.isGoalState(CurrentState):
            return Actions, len(Actions), ExpandedNodeCount

        # 4. 주변 노드(자식) 탐색
        for NextState, Action, Cost in problem.getSuccessors(CurrentState):
            # 5. 주변 노드가 아직 방문 전이라면
            if NextState not in Visited:
                # 즉시 방문 처리 후 큐에 추가
                Visited.add(NextState)
                Queue.append((NextState, Actions + [Action]))

    # 탐색 실패 시 반환
    return [], 0, ExpandedNodeCount
