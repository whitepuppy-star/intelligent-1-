# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.


import inspect
import sys
import random
from collections import deque
import heapq
import itertools


def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" %
          (method, line, fileName))
    sys.exit(1)


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        pass

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        pass

    def getSuccessors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        pass

    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        pass
    

def random_search(problem):
    """
    Search the nodes in the search tree randomly.

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm.

    This random_search function is just example not a solution.
    You can write your code by examining this function
    """
    start = problem.getStartState()
    node = [(start, "", 0)]   # class is better
    frontier = [node]

    explored = set()
    expanded_nodes = 0 

    while frontier:
        node = random.choice(frontier)
        state = node[-1][0]

        expanded_nodes += 1 

        if problem.isGoalState(state):
            return [x[1] for x in node][1:], expanded_nodes

        if state not in explored:
            explored.add(state)

            for successor in problem.getSuccessors(state):
                if successor[0] not in explored:
                    parent = node[:]
                    parent.append(successor)
                    frontier.append(parent)

    return [], expanded_nodes


def depth_first_search(problem):   
    # 1. 시작 상태와 빈 경로([])를 스택에 저장.
    # 스택 구조: (현재상태, 여기까지 오기위한 행동 리스트)
    start_node = (problem.getStartState(), [])
    stack = [start_node]
    
    # 2. 방문한 상태를 기록할 집합(set)을 생성. (Graph Search 필수!) 
    explored = set()

    while stack:
        # 3. 스택의 가장 마지막(최신) 노드 꺼내기.
        current_state, actions = stack.pop()

        # 4. 목표 상태(Goal)에 도달했는지 확인.
        if problem.isGoalState(current_state):
            return actions # 이동 경로 리스트 반환

        # 5. 아직 방문하지 않은 상태인 경우에만 자식 노드를 확장.
        if current_state not in explored:
            explored.add(current_state)

            # 6. 현재 상태에서 갈 수 있는 다음 노드들을 가져오기. 
            # successors: (다음 상태, 취한 행동, 이동 비용)의 리스트
            successors = problem.getSuccessors(current_state)

            for next_state, action, cost in successors:
                if next_state not in explored:
                    # 7. 새로운 경로를 생성하여 스택에 추가.
                    # 기존 actions 리스트에 현재의 action을 추가
                    new_actions = actions + [action]
                    stack.append((next_state, new_actions))

    # 탐색에 실패한 경우, 빈 리스트를 반환.
    return []    



def breadth_first_search(problem):
    # 1. 초기화: (현재 상태, 여기까지 오기 위한 행동 리스트)
    start_state = problem.getStartState()
    
    # 시작점이 이미 목표 상태인지 확인 (예외 처리)
    if problem.isGoalState(start_state):
        return []

    # FIFO 큐 생성: (상태, 경로)
    open_queue = deque([(start_state, [])])
    
    # 방문한 노드 기록 (중복 탐색 방지)
    closed_set = set()
    closed_set.add(start_state)

    # 2. 큐가 비어있지 않은 동안 반복
    while open_queue:
        # 가장 먼저 들어온 노드 꺼내기 (LIFO가 아닌 FIFO)
        current_state, actions = open_queue.popleft()

        # 현재 상태에서 갈 수 있는 다음 상태들 확장
        for next_state, action, cost in problem.getSuccessors(current_state):
            
            # 이미 방문한 적이 없는 새로운 상태라면
            if next_state not in closed_set:
                # 새로운 경로 생성
                new_actions = actions + [action]

                # 3. 목표 도달 확인 (Early Goal Test: 큐에 넣기 전 확인하여 성능 향상)
                if problem.isGoalState(next_state):
                    print(f"탐색 성공. 총 방문 노드 수: {len(closed_set)}")
                    return new_actions

                # 방문 처리 및 큐에 추가
                closed_set.add(next_state)
                open_queue.append((next_state, new_actions))

    # 경로를 찾지 못한 경우
    return []


def uniform_cost_search(problem):
    # 1. 초기화
    start_state = problem.getStartState()
    
    counter = itertools.count() # 중복 비교 방지를 위한 카운터

    # 우선순위 큐(PQ) 생성: (누적 비용, 현재 상태, 경로 리스트)
    # heapq는 첫 번째 요소인 '누적 비용'을 기준으로 최소 힙을 구성.
    pq = []
    heapq.heappush(pq, (0, next(counter), start_state, []))
    
    # 방문한 상태와 해당 상태까지의 최소 누적 비용 기록
    # {상태: 최소 누적 비용}
    visited = {}

    # 2. 탐색 루프
    while pq:
        # 누적 비용 g(n)이 가장 작은 노드를 꺼냄
        current_cost, _, current_state, actions = heapq.heappop(pq)

        # 목표 상태 도달 시 즉시 경로 반환 (최단 경로 보장)
        if problem.isGoalState(current_state):
            print(f"UCS 탐색, 최종 비용: {current_cost}")
            return actions

        # 이미 방문했더라도 현재 경로가 더 저렴한 경우에만 확장
        # 8-퍼즐처럼 비용이 모두 1인 경우, 먼저 도달한 것이 항상 최소 비용.
        if current_state not in visited or current_cost < visited[current_state]:
            visited[current_state] = current_cost

            # 자식 노드 확장
            for next_state, action, step_cost in problem.getSuccessors(current_state):
                # 새로운 누적 비용 계산: g(n) = 이전 비용 + 현재 이동 비용
                new_cost = current_cost + step_cost
                
                # 방문하지 않았거나 더 짧은(저렴한) 경로를 찾은 경우 큐에 추가
                if next_state not in visited or new_cost < visited.get(next_state, float('inf')):
                    new_actions = actions + [action]
                    heapq.heappush(pq, (new_cost, next(counter), next_state, new_actions))

    return []  # 경로를 찾지 못한 경우


def heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    "*** YOUR CODE HERE ***"
    return 0


def aStar_search(problem, heuristic=heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    raiseNotDefined()


# Abbreviations
rand = random_search
bfs = breadth_first_search
dfs = depth_first_search
astar = aStar_search
ucs = uniform_cost_search
