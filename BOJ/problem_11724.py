# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
# pypy3로 제출.

import sys


sys.setrecursionlimit(10000)
node_cnt, edge_cnt = map(int, input().split())

edge_list = [[] for _ in range(node_cnt+1)]
for _ in range(edge_cnt):
    first, second = map(int, input().split())
    edge_list[first].append(second)
    edge_list[second].append(first)

visited = [0] * (node_cnt+1)


def dfs(v):
    visited[v] = 1
    for i in edge_list[v]:
        if visited[i] == 0:
            dfs(i)


connected_component = 0
for i in range(1, node_cnt+1):
    if visited[i] == 0:
        dfs(i)
        connected_component += 1

print(connected_component)
