from collections import deque

def breadth_first_search(problem):
    # 1. 초기화 단계: open <- [시작노드], closed <- []
    StartState = problem.getStartState()

    # 시작하자마자 목표인지 확인 (예외 처리)
    if problem.isGoalState(StartState):
        return [], 0, 0

    # OpenList: 탐색 대기열 (FIFO 구조를 위해 deque 사용)
    # (현재 상태, 여기까지 오기 위한 행동 리스트) 형태로 저장
    OpenList = deque([(StartState, [])])
    
    # ClosedList: 이미 방문한 노드 기록 (중복 탐색 방지)
    # 리스트보다 탐색 속도가 훨씬 빠른 set 자료형 사용
    ClosedList = set([StartState]) 

    # 확장된 노드 수를 기록하는 변수
    ExpandedNodes = 0

    # 2. OpenList가 비어있지 않은 동안 반복 실행 (while open != [] do)
    while OpenList:
        # 3. X <- OpenList의 첫 번째 요소를 꺼냄 (FIFO 방식)
        CurrentState, Actions = OpenList.popleft()
        
        # 노드를 확장함 (자식 노드를 생성할 준비가 됨)
        ExpandedNodes += 1

        # 4. X의 자식 노드들을 생성 (Successors: 다음 상태, 행동, 비용)
        for NextState, action, cost in problem.getSuccessors(CurrentState):
            
            # 5. 자식 노드가 이미 ClosedList(방문 목록)에 있는지 확인
            # 이미 있다면 버리고, 없다면 계속 진행 (중복 제거)
            if NextState not in ClosedList:
                
                # 현재까지의 경로(Actions)에 이번에 취한 행동(action)을 추가
                NewActions = Actions + [action]

                # 6. if NextState == goal then return SUCCESS (목표 도달 확인)
                # 자식 노드를 생성하자마자 검사하여 탐색 속도를 높임 (조기 검사)
                if problem.isGoalState(NextState):
                    # 결과 반환: [경로 리스트], 경로 길이(Cost), 확장된 총 노드 수
                    return NewActions, len(NewActions), ExpandedNodes
                
                # 7. 방문한 적 없는 노드라면 ClosedList에 추가하고 OpenList 끝에 넣음
                ClosedList.add(NextState)       # 방문 표시
                OpenList.append((NextState, NewActions)) # 탐색 대기열 추가
                
    # 8. 모든 노드를 탐색했으나 목표를 찾지 못한 경우 (FAIL)
    return [], 0, ExpandedNodes
