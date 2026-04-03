def breadth_first_search(problem):
    # 초기화 하기 -> open : [시작노드], closed : []
    StartState = problem.getStartState()

    # 시작이 목표인지 확인
    if problem.isGoalState(StartState):
        return [], 0, 0

    # FIFO 구조라 deque 사용 (현재 상태, 여기까지 오기 위한 행동 리스트) 형태로 저장.
    OpenList = deque([(StartState, [])])
    # 중복 체크를 속도를 위해 set을 사용 (중복 방지)
    ClosedList = set([StartState]) 

    # 확장된 노드 수 
    ExpandedNodes = 0

    while OpenList:
        # open리스트의 첫번째 요소가 x가 됨. (FIFO) 
        CurrentState, Actions = OpenList.popleft()
        # 자식 노드를 생성할 준비
        ExpandedNodes+=1

        # x의 자식 노드들 생성 (Successors : 다음 상태, 행동, 비용)
        for NextState, action, cost in problem.getSuccessors(CurrentState):

            # 자식 노드가 이미 있다면 버리고, 없다면 계속 진행 (중복 방지를 위해)
            if NextState not in ClosedList:
                # 현재까지의 Actions에 이번에 취한 action 추가
                NewActions = Actions + [action]

                # 자식 노드 생성 후, 검사해 탐색 속도 높이기
                if problem.isGoalState(NextState):
                    # 경로 리스트, 경로 길이 (cost), 확장된 총 노드 수
                    return NewActions, len(NewActions), ExpandedNodes
                
                # 방문한 적이 없는 노드라면 ClosedList에 추가하고, OpenList 끝에 넣음.
                ClosedList.add(NextState)
                # 탐색 대기열에 추가
                OpenList.append((NextState, NewActions))

    # (실패) 모든 노드를 탐색했으나 목표를 찾지 못한 경우                
    return [], 0, ExpandedNodes
    
