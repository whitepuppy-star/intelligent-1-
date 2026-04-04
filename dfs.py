def depth_first_search(problem):
    # 1. 초기 설정 
    StartNode = problem.getStartState()
    # 방문한 상태를 기록할 셋
    Visited = set() 
    # 탐색할 노드를 담은 스택 (현재 상태, 그 상태까지의 경로)
    Stack = [(StartNode, [])] 
    
    ExpandedNodeCount = 0  # 확장한 노드 수 기록용 

    while Stack:
        # 2. 스택에서 하나를 꺼냄. NextState는 CurrentState로. 경로리스트는 Actions 변수로.
        CurrentState, Actions = Stack.pop() 

        # 3. 목표 상태인지 확인. 목표라면 (경로, 경로 길이, 확장 노드 수) 반환.
        if problem.isGoalState(CurrentState): 
            return Actions, len(Actions), ExpandedNodeCount 

        # 4. 방문 여부 체크 
        if CurrentState not in Visited: 
            Visited.add(CurrentState) 
            ExpandedNodeCount += 1 

            # 5. 주변 노드(자식) 탐색
            for NextState, Action, Cost in problem.getSuccessors(CurrentState):
                # 6. 주변 노드가 아직 탐색 전이라면 스택에 추가
                if NextState not in Visited:
                    Stack.append((NextState, Actions + [Action])) # 자식 노드를 스택에 튜플로 추가.

    # 탐색 실패 시 None이 아닌 빈 값들을 반환 (에러 방지)
    return [], 0, ExpandedNodeCount 

