def h_manhattan(state):
    # state.cells는 2차원 리스트 형태.
    Distance = 0
    
    for i in range(3):
        for j in range(3):
            # 현재 칸의 숫자 확인
            Value = state.cells[i][j]
            
            # 빈칸(0)이 아닐 때만 거리를 계산함
            if Value != 0:
                # divmod를 사용하여 목표 행(x)과 목표 열(y)을 한 번에 계산
                # (Value - 1)을 3으로 나눈 몫이 행, 나머지가 열이 됨
                TargetRow, TargetCol = divmod(Value - 1, 3)
                
                # 현재 위치(i, j)와 목표 위치 사이의 절대 거리 합산
                Distance += abs(TargetRow - i) + abs(TargetCol - j)
                
    return Distance
