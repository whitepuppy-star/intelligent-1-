def depth_first_search(problem):
    # 시작 상태와 빈 경로를 스택에 저장. 스택 구조 : (현재 상태, 여기까지 오기위한 행동 리스트)
    StartNode = (problem.getStartState(), [])
    stack = [StartNode]

    # 방문한 상태를 기록할 set을 생성. (그래프 탐색이니까)
    explored = set()

    expandedNode = 0

    while stack:
        # 스택의 가장 마지막 노드 꺼내기
        CurrentState, actions = stack.pop()

        # 목표 상태에 도달했는지 확인하기
        if problem.isGoalState(CurrentState):
            return actions, len(actions), len(explored)
        
        # 아직 방문하지 않은 경우멘 자식 노드를 확장
        if CurrentState not in explored:
            explored.add(CurrentState)
            expandedNode += 1

            # 현재 상태에서 갈 수 있는 다음 노드들을 가져오기
            # successors 리스트 (다음 상태, 취한 행동, 이동 비용)
            successors = problem.getSuccessors(CurrentState)

            for NextState, action, cost in successors:
                if NextState not in explored:
                    # 새로운 경로를 생성하여 스택에 추가
                    # 기존 actions 리스트에 현재의 action을 추가
                    NewAction = actions + [action]
                    stack.append((NextState, NewAction))

    # 탐색 실패한 경우, 빈 리스트 반환
    return [], 0, expandedNode

