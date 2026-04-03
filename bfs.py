from collections import deque

def breadth_first_search(problem):
    # 1. open <- [시작노드], closed <- []
    # (state, actions) 튜플을 담아 경로를 추적합니다.
    start_state = problem.getStartState()
    open_list = deque([(start_state, [])])
    closed_list = set() # 효율적인 중복 체크를 위해 set 사용
    
    expanded_nodes = 0

    # 2. while open != [] do
    while open_list:
        # 3. X <- open 리스트의 첫 번째 요소 (FIFO)
        current_state, actions = open_list.popleft()
        
        # 4. if X == goal then return SUCCESS
        if problem.isGoalState(current_state):
            return actions, len(actions), expanded_nodes
        
        # 5. X를 closed 리스트에 추가한다.
        if current_state not in closed_list:
            closed_list.add(current_state)
            expanded_nodes += 1
            
            # 6. X의 자식 노드를 생성한다.
            successors = problem.getSuccessors(current_state)
            
            for next_state, action, cost in successors:
                # 7. 자식 노드가 이미 open이나 closed에 있다면 버린다.
                # (이미 open에 있는 노드를 중복 추가하지 않기 위해 체크)
                if next_state not in closed_list and next_state not in [node[0] for node in open_list]:
                    # 8. 남은 자식 노드들은 open의 끝에 추가한다.
                    new_actions = actions + [action]
                    open_list.append((next_state, new_actions))
                    
    # 9. return FAIL
    return [], 0, expanded_nodes
