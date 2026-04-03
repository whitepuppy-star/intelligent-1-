def uniform_cost_search(problem):
    # 시작 상태
    StartState = problem.getStartState()

    # 비용이 같으니 객체 대신 숫자로 비교하게 만들기.
    # 큐 초기화
    count = 0
    # 우선 순위 큐 초기화 : 누적 비용, 고유번호, 상태, 경로
    queue = [(0, count, StartState, [])]

    #중복 방지를 위해 방문 기록 (리스트보다 빠른 set 사용)
    visited = set()
    ExpandedNodes = 0

    while queue:

        # count 변수를 받아줄 자리 만들기. 총 4개로.
        # 이때 비용이 가장 적은 노드를 큐에서 꺼냄 (priority queue)
        CurrentCost, _, CurrentState, actions = heapq.heappop(queue)

        # 여기서 방문 체크. (중복 방지)
        if CurrentState in visited:
            continue

        # 방문 처리 및 확장 노드 수 증가
        visited.add(CurrentState)
        ExpandedNodes+=1
        
        # 목표 상태 도달 확인 
        if problem.isGoalState(CurrentState):
            return actions, len(actions), ExpandedNodes
        
        # 인접합 자식 노드들 확장
        for NextState, action, StepCost in problem.getSuccessors(CurrentState):
            # 큐에 넣기 전에 미리 확인.
            if NextState not in visited:
               
               # 시작점부터 누적 비용 계산하기
                NewCost = CurrentCost + StepCost
                NewActions = actions + [action]

                # 수정. 비용이 같으니 count 숫자로 비교하고 넘어가게 만듦.
                count += 1
                heapq.heappush(queue, (NewCost, count, NextState, actions + [action]))

    #탐색 실패 시 빈 결과 반환
    return [], 0, ExpandedNodes
