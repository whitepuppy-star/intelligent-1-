import copy

def checkZero(puzzle):
    """현재 퍼즐에서 빈 공간(0)의 좌표(x, y)를 반환합니다."""
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '0':
                return i, j
    return None

def movePuzzle(puzzle, x, y, op):
    """지정된 연산(up, down, left, right)에 따라 퍼즐을 이동시킵니다."""
    nx, ny = x, y
    if op == 'up':
        nx -= 1
    elif op == 'down':
        nx += 1
    elif op == 'left':
        ny -= 1
    elif op == 'right':
        ny += 1

    # 퍼즐판 범위를 벗어나는지 체크
    if 0 <= nx < 3 and 0 <= ny < 3:
        # 빈 공간('0')과 인접 타일을 교체 (Swap)
        puzzle[x][y], puzzle[nx][ny] = puzzle[nx][ny], puzzle[x][y]
        return puzzle
    else:
        return None

def bfs(puzzle):
    visit = []
    queue = [puzzle]
    # 목표 상태 (이미지 기준)
    goal = [['1', '2', '3'], ['8', '0', '4'], ['7', '6', '5']]
    oper = ['up', 'down', 'right', 'left']

    # queue가 비어있지 않은 동안 반복 (이미지의 is not None을 리스트 조건으로 수정)
    while queue:
        current = queue.pop(0)

        # 현재 상태가 목표 상태와 같은지 확인
        if current == goal:
            visit.append(current)
            return visit
        
        # 이미 방문한 노드라면 건너뛰기 (성능 최적화를 위해 append 전보다 pop 직후 체크가 유리)
        if current in visit:
            continue
            
        visit.append(current)
        x, y = checkZero(current)

        for op in oper:
            # 원본 보존을 위해 deepcopy 사용
            next_state = movePuzzle(copy.deepcopy(current), x, y, op)

            if next_state is not None and next_state not in visit and next_state not in queue:
                queue.append(next_state)

    return None

# 실행 예시
start_node = [['1', '2', '3'], ['0', '8', '4'], ['7', '6', '5']]
result = bfs(start_node)

if result:
    print(f"탐색 성공! 총 {len(result)}개의 상태를 거쳤습니다.")
    for idx, state in enumerate(result):
        print(f"Step {idx}: {state}")
else:
    print("해를 찾을 수 없습니다.")
